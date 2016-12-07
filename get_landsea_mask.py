from ecmwfapi import ECMWFDataServer

if __name__ == '__main__':
    server = ECMWFDataServer()

    server.retrieve({
        "class": "ti",
        "dataset": "tigge",
        "date": "2012-01-01/2013-01-01",
        "expver": "prod",
        "grid": "0.5/0.5",
        "levtype": "sfc",
        "origin": "ecmf",
        "param": "172",
        "area": "-33/135/-41/150",
        "step": "0/6/12/18/24/30/36/42/48/54/60/66/72",
        "time": "00:00:00",
        "type": "fc",
        "target": "landseamask",
    })
