import logging
import sys

from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

# TODO:
#  1. Change print into logging?
#  2. Identical relation a->a checking?


class App:

    def __init__(self, url, user, password):
        self.driver = GraphDatabase.driver(url, auth=(user, password))

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()

    @staticmethod
    def enable_log(level, output_stream):
        handler = logging.StreamHandler(output_stream)
        handler.setLevel(level)
        logging.getLogger("neo4j").addHandler(handler)
        logging.getLogger("neo4j").setLevel(level)

    def clear_all(self):
        with self.driver.session() as session:
            result = session.write_transaction(
                self._clear_all_return)
            return result

    @staticmethod
    def _clear_all_return(tx):
        result = tx.run("MATCH (n) DETACH DELETE n")
        return result

    def create_pm_prop(self, pnum, vol, part, sect, pg, tp):
        if self.check_prop_exists(pnum):
            print("Proposition {pnum} {tp}(updated)".format(pnum=pnum, tp=tp))
            with self.driver.session() as session:
                result = session.write_transaction(
                    self._update_pm_prop_and_return, pnum, vol, part, sect, pg, tp)
        else:
            print("Proposition {pnum} {tp}".format(pnum=pnum, tp=tp))
            with self.driver.session() as session:
                result = session.write_transaction(
                    self._create_pm_prop_and_return, pnum, vol, part, sect, pg, tp)

    @staticmethod
    def _create_pm_prop_and_return(tx, pnum, vol, part, sect, pg, tp):
        ch, thm = pnum.split(".")
        node = "n" + ch + "_" + thm
        result = tx.run(
            "CREATE(" + node + ":Prop" +
            "{volume:'" + vol + "'," +
            "part:'" + part + "'," +
            "section:'" + sect + "'," +
            "chapter:'" + ch + "'," +
            "number:'" + pnum + "'," +
            "page:'" + pg + "'," +
            "type:'" + tp + "'})")
        return result

    @staticmethod
    def _update_pm_prop_and_return(tx, pnum, vol, part, sect, pg, tp):
        ch, thm = pnum.split(".")
        result = tx.run(
            "MATCH (p:Prop {number: '" + pnum + "'}) " +
            "SET p.volume='" + vol + "'," +
            "p.part='" + part + "'," +
            "p.section='" + sect + "'," +
            "p.chapter='" + ch + "'," +
            "p.number='" + pnum + "'," +
            "p.page='" + pg + "'," +
            "p.type='" + tp + "'")
        return result

    def connect_pm(self, p1, p2):
        if not self.check_prop_exists(p1):
            print("{p1} not found for {p1}->{p2}".format(p1=p1, p2=p2))
        elif not self.check_prop_exists(p2):
            print("{p2} not found for {p1}->{p2}".format(p1=p1, p2=p2))
        elif not self.check_conn_exists(p1, p2):
            print(p1 + " -[Proves]-> " + p2)
            with self.driver.session() as session:
                result = session.write_transaction(self._connect_pm_prop, p1, p2)
                return result
        else:
            print("{p1} -[Proves]-> {p2}(already exists)".format(p1=p1, p2=p2))
        return None

    @staticmethod
    def _connect_pm_prop(tx, p1, p2):
        result = tx.run(
            "MATCH (a:Prop {number: '" + p1 + "'}) " +
            "MATCH (b:Prop {number: '" + p2 + "'})" +
            "CREATE (a)-[r:Proves]->(b)")
        return result

    def update_prop_name(self, p, name):
        # BUG: Cannot delete a prop's name if already assigned.
        if self.check_prop_exists(p):
            with self.driver.session() as session:
                result = session.write_transaction(self._update_prop_name_return, p, name)
                return result
        else:
            print("No proposition {p} found in database for name {name}".format(p=p, name=name))
            pass

    @staticmethod
    def _update_prop_name_return(tx, p, name):
        result = tx.run(
            "MATCH (a:Prop {number: '" + p + "'})" +
            "SET a.name = '" + name + "'"
        )
        return result

    def check_prop_exists(self, p):
        with self.driver.session() as session:
            result = session.read_transaction(self._check_prop_exists_return, p)
            return False if result == 0 else True
            # return result

    @staticmethod
    def _check_prop_exists_return(tx, p):
        query = "MATCH (n:Prop {number: '" + p + "'}) " + "RETURN count(n) AS count"
        result = tx.run(query).single()
        try:
            count = result["count"]
            return count
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise

    def check_conn_exists(self, p1, p2):
        with self.driver.session() as session:
            result = session.read_transaction(self._check_conn_exists_return, p1, p2)
            return False if result == 0 else True

    @staticmethod
    def _check_conn_exists_return(tx, p1, p2):
        query = "MATCH " \
                "(p1:Prop {number: '" + p1 + "'})" \
                "-[r:Proves]->" \
                "(p2:Prop {number: '" + p2 + "'}) " \
                "RETURN count(r) AS count"
        result = tx.run(query).single()
        try:
            count = result["count"]
            return count
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise






