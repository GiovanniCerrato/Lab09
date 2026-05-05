from database.DAO import DAO
DAO = DAO()
print(*(f"{v}\n" for v in DAO.getPossibiliEdges()))