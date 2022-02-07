import logging
import sys

from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

# TODO: change print into logging?


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

    def create_pm_prop(self, pnum, vol, part, sect, pg, tp):
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

    def connect_pm(self, p1, p2):
        print(p1 + " -> " + p2 + " ...")

        with self.driver.session() as session:
            result = session.write_transaction(self._connect_pm_prop, p1, p2)

        print("Relation " + p1 + " -> " + p2 + " created")

    @staticmethod
    def _connect_pm_prop(self, tx, p1, p2):
        result = tx.run(
            "MATCH (a:Prop {number: '" + p1 + "'}), " +
            "(b:Prop {number: '" + p2 + "'})" +
            "CREATE (a)-[r:proves]->(b)")
        return result

    def update_prop(self, pnum, vol, part, sect, pg, tp):
        print("Proposition {pnum} {tp} updated".format(pnum=pnum, tp=tp))
        with self.driver.session() as session:
            result = session.write_transaction(
                self._update_prop_return, pnum, vol, part, sect, pg, tp)

    def update_prop_name(self, p, name):
        with self.driver.session() as session:
            result = session.write_transaction(self._update_prop_name_return, p, name)

    @staticmethod
    def _update_prop_name_return(self, tx, p, name):
        if self.check_prop_exists(p):
            result = tx.run(
                "MATCH (a:Prop {number: " + p + "})" +
                "SET a.name = '" + name + "'"
            )
        else:
            print("No proposition {p} found in database for name {name}".format(p=p, name=name))
            pass
        pass

    @staticmethod
    def _update_prop_return(self, tx, pnum, vol, part, sect, pg, tp):
        # TODO: SET...
        pass

    def check_prop_exists(self, p):
        with self.driver.session() as session:
            result = session.write_transaction(self. _check_prop_exists_return, p)

    @staticmethod
    def _check_prop_exists_return(self, tx, p):
        query = "MATCH (a:Prop {number: " + p + "}) " + "RETURN count(n) AS count"
        result = tx.run(query)
        try:
            count = result["count"]
            return False if count == 0 else True
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise


