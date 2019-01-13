# MAT Fan Engagement Coding Challenge

## Prerequisites:

* [docker](https://docs.docker.com/)
* [docker-compose](https://docs.docker.com/compose/)

## Introduction

The purpose of this challenge is to demonstrate how you:

* write and structure a simple backend application in an appropriate language of your choice
* parse and transform streamed telemetry data
* deliver a component to integrate into a stack of technologies

Feel free to use any libraries, frameworks or dependencies you want in order to achieve the task.

Include instructions for how to build and run your code, any tests you've written and some text explaining what you did.

If you are already familiar with the underlying technologies we hope that it won't take you more than a couple of hours to get your application up and running.

## Scenario

Live data from a Formula 1 race has been recorded and streamed into our system. We want to use that data in order to engage fans by providing a live visualization.

## Challenge

Raw telemetry data is arriving via MQTT. A basic front-end application has been developed to visualize cars going around a track. It can also display an event stream and car status information such as speed and position, but currently it is not receiving this information.

Please develop a data processing application which subscribes to the provided MQTT broker and consumes data from the following MQTT topic:

* **carCoordinates**

    ```console
      {
        timestamp: number,
        carIndex: number,
        location: {
          lat: float,
          long: float
         }
      }
    ```

  e.g.

    ```json
      {
        "timestamp": 1541693114862,
        "carIndex": 2,
        "location": {
          "lat": 51.349937311969725,
          "long": -0.544958142167281
         }
      }
    ```

And then publishes aggregated and enriched data on the following MQTT topics:

- **carStatus**

    ```console
      {
        timestamp: number,
        carIndex: number,
        type: string<SPEED|POSITION>,
        value: number
      }
    ```

  e.g.

    ```json
      {
        "timestamp": 1541693114862,
        "carIndex": 2,
        "type": "POSITION",
        "value": 1
      }
    ```

- **events**

    ```console
      {
        timestamp: number,
        text: string
      }
    ```

  e.g.

    ```json
      {
        "timestamp": 1541693114862,
        "text": "Car 2 races ahead of Car 4 in a dramatic overtake."
      }
    ```

All these topics will then be forwarded via a gateway-like MQTT to Web Sockets service to the frontend application.

## Architecture

![Components](./components.svg)

## Getting started

Start all components:

```console
$ docker-compose pull
$ docker-compose up -d
Creating network "mat-coding-challenge_default" with the default driver
Creating broker ... done
Creating source_gps        ... done
Creating mqtt-to-websocket ... done
Creating webapp            ... done
```

Open (http://localhost:8084)

Test the setup with `mosquitto_pub` or a similar MQTT client:

```console
$ mosquitto_pub -t events -f examples/event.json
$ mosquitto_pub -t carStatus -f examples/status.json
```

You should now see a car's position and an event in the webapp.
