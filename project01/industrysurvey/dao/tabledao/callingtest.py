from dao.tabledao.Intetfacecrud import Report
from dao.tabledao.CustomerMasterDAO import Instert,Update
if __name__ == "__main__":


    report = Report("test report",Instert())
    report.printer()

