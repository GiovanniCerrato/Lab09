from database.DB_connect import DBConnect
from model.arco import Arco
from model.volo import Volo


class DAO():

    @staticmethod
    def getPossibiliEdges():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []
        query = """SELECT
                    LEAST(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID) as a1,
                    GREATEST(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID) as a2,
                    AVG(f.DISTANCE) as distanzaMediaPercorsa
                    FROM flights f
                    GROUP BY a1, a2;"""

        cursor.execute(query)
        for row in cursor:
            res.append(Arco(**row))
        cursor.close()
        conn.close()
        return res
