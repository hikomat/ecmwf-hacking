from ecmwfapi import ECMWFDataServer

if __name__ == '__main__':
    server = ECMWFDataServer()

    server.retrieve({
        "class": "ti",
        "dataset": "tigge",
        "date": "2012-01-01/to/2012-12-31",
        "expver": "prod",
        "grid": "0.5/0.5",
        "levtype": "sfc",
        "origin": "ecmf",
        "param": "59/151/165/166/167",
        "area": "-33/135/-41/150",
        "step": "0/6/12/18/24/30/36/42/48/54/60/66/72",
        "time": "00:00:00",
        "type": "fc",
        "target": "2012fc",
    })

    server.retrieve({
        "class": "ti",
        "dataset": "tigge",
        "date": "2012-01-01/to/2012-12-31",
        "expver": "prod",
        "grid": "0.5/0.5",
        "levtype": "sfc",
        "origin": "ecmf",
        "param": "59/151/165/166/167",
        "area": "-33/135/-41/150",
        "step": "0/6/12/18/24/30/36/42/48/54/60/66/72",
        "time": "00:00:00",
        "type": "cf",
        "target": "2012cf",
    })

    server.retrieve({
        "class": "ti",
        "dataset": "tigge",
        "date": "2013-01-01/to/2013-12-31",
        "expver": "prod",
        "grid": "0.5/0.5",
        "levtype": "sfc",
        "origin": "ecmf",
        "param": "59/151/165/166/167",
        "area": "-33/135/-41/150",
        "step": "0/6/12/18/24/30/36/42/48/54/60/66/72",
        "time": "00:00:00",
        "type": "fc",
        "target": "2013fc",
    })

    server.retrieve({
        "class": "ti",
        "dataset": "tigge",
        "date": "2013-01-01/to/2013-12-31",
        "expver": "prod",
        "grid": "0.5/0.5",
        "levtype": "sfc",
        "origin": "ecmf",
        "param": "59/151/165/166/167",
        "area": "-33/135/-41/150",
        "step": "0/6/12/18/24/30/36/42/48/54/60/66/72",
        "time": "00:00:00",
        "type": "cf",
        "target": "2013cf",
    })
