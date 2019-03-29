# Concern Definition (Events)

**Concern-Tag :** `events`

This is all about events.

## General Parameters

* **type** (dictionary) "events"
* **events** (array of dictionaries) Array of events for the given parameters

## Request Types

**Type-Tag:** `event_pollination`

#### Request

- **location** (string): Coordinates of interest
- **start_date** (string): start date in the format 'year-month-day'
- **end_date** (string): end date in the format 'year-month-day'

#### Response

- **type**: String as listed in general parameters
- **events**: Array as listed in general parameters

#### Example

Request

```json
{
	"payload": {
		"categories": ["concerts", "performing-arts"],
                "location": "@48.7744476,9.1714984,17.5",
                "start_date": "2019-03-29",
                "end_date": "2019-04-30"
	},
	"type": "current_events"
}
```

Response

```json
[
  {
    "payload": {
      "events": [
        {
          "category": "concerts",
          "description": "",
          "location": [
            9.16122,
            48.770088
          ],
          "start": "2019-04-27T19:00:00Z",
          "title": "Bernd Begemann - Der elektrische Liedermacher"
        },
        {
          "category": "concerts",
          "description": "",
          "location": [
            8.99412,
            48.70732
          ],
          "start": "2019-04-27T18:30:00Z",
          "title": "Kaisers Bart \\u201cMeister5tück\\u201c - Deutsch-Metal-Inszenierung"
        },
        {
          "category": "concerts",
          "description": "",
          "location": [
            9.179198,
            48.772507
          ],
          "start": "2019-04-27T18:00:00Z",
          "title": "The Wild Rumble"
        },
        {
          "category": "concerts",
          "description": "",
          "location": [
            9.17703,
            48.7751
          ],
          "start": "2019-04-27T18:00:00Z",
          "title": "Sudden Stuttgart"
        },
        {
          "category": "performing-arts",
          "description": "",
          "location": [
            9.176299,
            48.772655
          ],
          "start": "2019-04-27T18:30:00Z",
          "title": "Heimat.Museum - Premiere"
        },
        {
          "category": "performing-arts",
          "description": "",
          "location": [
            9.179123,
            48.810253
          ],
          "start": "2019-04-27T18:15:00Z",
          "title": "Die Hölle des positiven Denkens - Derniere"
        },
        {
          "category": "performing-arts",
          "description": "",
          "location": [
            9.173053,
            48.777969
          ],
          "start": "2019-04-27T18:00:00Z",
          "title": "Renitenz-Ensemble - Wohin mit Stuttgart?"
        },
        {
          "category": "performing-arts",
          "description": "",
          "location": [
            9.181038,
            48.786778
          ],
          "start": "2019-04-27T18:00:00Z",
          "title": "Quatsch Comedy Club - Die Live Show - mit: Thomas Schmidt, Diva La Kruttke, Der Bembers und Nils Heinrich. Mod.: Costa Meronianakis"
        },
        {
          "category": "performing-arts",
          "description": "",
          "location": [
            9.173719,
            48.772982
          ],
          "start": "2019-04-27T18:00:00Z",
          "title": "Wie es euch gefällt - William Shakespeare"
        },
        {
          "category": "performing-arts",
          "description": "",
          "location": [
            9.202582,
            48.792319
          ],
          "start": "2019-04-27T18:00:00Z",
          "title": "Sprich zu mir (auf Russisch)"
        }
      ]
    },
    "type": "event"
  }
]
```



