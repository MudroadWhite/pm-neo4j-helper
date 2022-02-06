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
        print("Creating proposition {pnum}...".format(pnum=pnum))

        with self.driver.session() as session:
            result = session.write_transaction(
                self._create_pm_prop_and_return, pnum, vol, part, sect, pg, tp)

    @staticmethod
    def _create_pm_prop_and_return(tx, pnum, vol, part, sect, pg, tp):
        ch, thm = pnum.split(".")
        node = "n" + ch + "_" + thm
        query = (
            "CREATE(" + node + ":Prop" +
            "{volume:'" + vol + "'," +
            "part:'" + part + "'," +
            "section:'" + sect + "'," +
            "chapter:'" + ch + "'," +
            "number:'" + pnum + "'," +
            "page:'" + pg + "'," +
            "type:'" + tp + "'})")
        result = tx.run(query)
        return result

    def connect_pm(self, p1, p2):
        print(p1 + " -> " + p2 + " ...")

        with self.driver.session() as session:
            result = session.write_transaction(self._connect_pm_prop, p1, p2)

        print("Relation " + p1 + " -> " + p2 + " created")

    def _connect_pm_prop(self, tx, p1, p2):
        query = (
            "MATCH (a:Prop), (b:Prop) WHERE " +
            "a.number = '" + p1 + "' AND b.number = '" + p2 + "' " +
            "CREATE (a)-[r:proves]->(b)")
        result = tx.run(query)
        return result


