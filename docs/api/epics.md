# Epics API documentation

## 14. Epics

### 14.1. List

To list epics send a GET request with the following parameters:

```bash
curl -X GET \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${AUTH_TOKEN}" \
    -s http://localhost:8000/api/v1/epics
```

The HTTP response is a 200 OK and the response body is a JSON list of epic list objects

The results can be filtered using the following parameters:

- project: project id
- project__slug: project slug
- assigned_to: assigned to user id
- status__is_closed: boolean indicating if the epic status is closed

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epics?project=1>
14.2. Create
To create epics send a POST request with the following data:

assigned_to: user id

blocked_note: reason why the epic is blocked

description: string

is_blocked: boolean

is_closed: boolean

color: HEX color

project (required): project id

subject (required)

tags: array of strings

watchers: array of watcher id’s

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "assigned_to": null,
        "blocked_note": "blocking reason",
        "client_requirement": false,
        "color": "#ABCABC",
        "description": "New epic description",
        "epics_order": 2,
        "is_blocked": true,
        "project": 1,
        "status": 2,
        "subject": "New epic",
        "tags": [
            "service catalog",
            "customer"
        ],
        "team_requirement": false,
        "watchers": []
    }' \
-s http://localhost:8000/api/v1/epics
curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "project": 1,
        "subject": "New epic"
    }' \
-s <http://localhost:8000/api/v1/epics>
When the creation is successful, the HTTP response is a 201 Created and the response body is a JSON epic detail object

14.3. Get
To get an epic send a GET request specifying the epic id in the url

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epics/1>
The HTTP response is a 200 OK and the response body is a JSON epic detail (GET) object

14.4. Get by ref
To get an epic send a GET request specifying the epic reference and one of the following parameters:

project (project id)

project__slug

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epics/by_ref?ref=121\&project=3>
The HTTP response is a 200 OK and the response body is a JSON epic detail (GET) object

14.5. Edit
To edit epics send a PUT or a PATCH specifying the epic id in the url. In a PATCH request you just need to send the modified data, in a PUT one the whole object must be sent.

curl -X PATCH \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "subject": "Patching subject",
        "version": 1
    }' \
-s <http://localhost:8000/api/v1/epics/15>
When the creation is successful, the HTTP response is a 200 OK and the response body is a JSON epic detail object

14.6. Delete
To delete epics send a DELETE specifying the epic id in the url

curl -X DELETE \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epics/15>
When delete succeeded, the HTTP response is a 204 NO CONTENT with an empty body response

14.7. Bulk creation
To create multiple epics at the same time send a POST request with the following data:

project_id (required)

status_id (optional)

bulk_epics: epic subjects, one per line

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "bulk_epics": "EPIC 1 \n EPIC 2 \n EPIC 3",
        "project_id": 1
    }' \
-s <http://localhost:8000/api/v1/epics/bulk_create>
When the creation is successful, the HTTP response is a 200 OK and the response body is a JSON list of epic detail object

14.8. Filters data
To get the epic filters data send a GET request specifying the project id in the url

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epics/filters_data?project=1>
The HTTP response is a 200 OK and the response body is a JSON epic filters data object

14.9. List related userstories
To get the list of related user stories from an epic send a GET request specifying the epic id in the url

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epics/15/related_userstories>
The HTTP response is a 200 OK and the response body is a JSON list of epic related user story detail objects

14.10. Create related userstory
To create an epic related user story send a POST request with the following data:

epic: related epic id

user_story: related user story id

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "epic": 15,
        "user_story": 1
    }' \
-s <http://localhost:8000/api/v1/epics/15/related_userstories>
When the creation is successful, the HTTP response is a 201 Created and the response body is a JSON epic related user story detail object

14.11. Get related userstory
To get a related user story from an epic send a GET request specifying the epic and user story ids in the url

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epics/15/related_userstories/2>
The HTTP response is a 200 OK and the response body is a JSON epic related user story detail object

14.12. Edit related userstory
To edit epic related user stories send a PUT or a PATCH specifying the epic and user story ids in the url. In a PATCH request you just need to send the modified data, in a PUT one the whole object must be sent.

curl -X PATCH \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "order": 100
    }' \
-s <http://localhost:8000/api/v1/epics/15/related_userstories/2>
When the creation is successful, the HTTP response is a 200 OK and the response body is a JSON epic related user story detail object

14.13. Delete related userstory
To delete epic related user stories send a DELETE specifying the epic and the userstory ids in the url

curl -X DELETE \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epics/15/related_userstories/2>
When delete succeeded, the HTTP response is a 204 NO CONTENT with an empty body response

14.14. Bulk related userstories creation
To create multiple related user stories at the same time send a POST request with the following data:

project_id (required)

bulk_userstories: user stories subjects, one per line

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "bulk_userstories": "epic 1 \n epic 2 \n epic 3",
        "project_id": 3
    }' \
-s <http://localhost:8000/api/v1/epics/15/related_userstories/bulk_create>
When the creation is successful, the HTTP response is a 201 OK and the response body is a JSON list of epic related user story detail object

14.15. Vote an epic
To vote epics send a POST request specifying the epic id in the url

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epics/3/upvote>
The HTTP response is a 200 OK with an empty body response

14.16. Remove vote from an epic
To remove a vote from an epic send a POST request specifying the epic id in the url

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epics/3/downvote>
When remove of the vote succeeded, the HTTP response is a 200 OK with an empty body response

14.17. Get epic voters list
To get the list of voters from an epic send a GET request specifying the epic id in the url

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epics/1/voters>
The HTTP response is a 200 OK and the response body is a JSON list of epic voter object

14.18. Watch an epic
To watch an epic send a POST request specifying the epic id in the url

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epics/15/watch>
The HTTP response is a 200 OK with an empty body response

14.19. Stop watching an epic
To stop watching an epic send a POST request specifying the epic id in the url

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epics/15/unwatch>
The HTTP response is a 200 OK with an empty body response

14.20. List epic watchers
To get the list of watchers from an epic send a GET request specifying the epic id in the url

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epics/15/watchers>
The HTTP response is a 200 OK and the response body is a JSON list of epic watcher object

14.21. List attachments
To list epic attachments send a GET request with the following parameters:

project: project id

object_id: epic id

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epics/attachments?object_id=773\&project=1>
The HTTP response is a 200 OK and the response body is a JSON list of attachment detail objects

14.22. Create attachment
To create epic attachments send a POST request with the following data:

object_id (required): epic id

project (required): project id

attached_file (required): attaching file

description

is_deprecated

curl -X POST \
-H "Content-Type: multipart/form-data" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-F attached_file=@test.png \
-F from_comment=False \
-F object_id=15 \
-F project=3 \
-s <http://localhost:8000/api/v1/epics/attachments>
When the creation is successful, the HTTP response is a 201 Created and the response body is a JSON attachment detail object

14.23. Get attachment
To get an epic attachment send a GET request specifying the epic attachment id in the url

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epics/attachments/773>
The HTTP response is a 200 OK and the response body is a JSON attachment detail object

14.24. Edit attachment
To edit epic attachments send a PUT or a PATCH specifying the epic attachment id in the url. In a PATCH request you just need to send the modified data, in a PUT one the whole object must be sent.

curl -X PATCH \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "description": "Updated description"
    }' \
-s <http://localhost:8000/api/v1/epics/attachments/773>
When the creation is successful, the HTTP response is a 200 OK and the response body is a JSON attachment detail object

14.25. Delete attachment
To delete epic attachments send a DELETE specifying the epic attachment id in the url

curl -X DELETE \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epics/attachments/773>
When delete succeeded, the HTTP response is a 204 NO CONTENT with an empty body response

1. Epic status
15.1. List
To list epic status send a GET request with the following parameters:

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epic-statuses>
The HTTP response is a 200 OK and the response body is a JSON list of epic status detail objects

The results can be filtered using the following parameters:

project: project id

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epic-statuses?project=1>
15.2. Create
To create epic statuses send a POST request with the following data:

color: in hexadecimal

is_closed: (true|false)

name (required)

order: integer

project: (required): project id

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "color": "#AAAAAA",
        "is_closed": true,
        "name": "New status",
        "order": 8,
        "project": 1
    }' \
-s http://localhost:8000/api/v1/epic-statuses
curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "name": "New status name",
        "project": 1
    }' \
-s <http://localhost:8000/api/v1/epic-statuses>
When the creation is successful, the HTTP response is a 201 Created and the response body is a JSON epic status detail object

15.3. Get
To get an epic status send a GET request specifying the epic status id in the url

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epic-statuses/1>
The HTTP response is a 200 OK and the response body is a JSON epic status detail object

15.4. Edit
To edit epic statuses send a PUT or a PATCH specifying the epic status id in the url. In a PATCH request you just need to send the modified data, in a PUT one the whole object must be sent.

curl -X PATCH \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "name": "Patch status name"
    }' \
-s <http://localhost:8000/api/v1/epic-statuses/1>
When the creation is successful, the HTTP response is a 200 OK and the response body is a JSON epic status detail object

15.5. Delete
To delete epic satuses send a DELETE specifying the epic status id in the url

curl -X DELETE \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epic-statuses/1>
When delete succeeded, the HTTP response is a 204 NO CONTENT with an empty body response

15.6. Bulk update order
To update the order of multiple epic statuses at the same time send a POST request with the following data:

project (required)

bulk_epic_statuses: list where each element is a list, the first element is the status id and the second the new order

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "bulk_epic_statuses": [
            [
                1,
                10
            ],
            [
                2,
                5
            ]
        ],
        "project": 1
    }' \
-s <http://localhost:8000/api/v1/epic-statuses/bulk_update_order>
When the update is successful, the HTTP response is a 204 NO CONTENT with an empty body response

1. Epic custom attribute
16.1. List
To list epic custom attributes send a GET request with the following parameters:

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epic-custom-attributes>
The HTTP response is a 200 OK and the response body is a JSON list of epic custom attribute detail objects

The results can be filtered using the following parameters:

project: project id

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epic-custom-attributes?project=1>
16.2. Create
To create epic custom attributes send a POST request with the following data:

name: (required) text

description: text

order: integer

project: (required) integer, project id

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "description": "Duration in minutes",
        "name": "Duration 2",
        "order": 8,
        "project": 1
    }' \
-s http://localhost:8000/api/v1/epic-custom-attributes
curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "name": "Duration 3",
        "project": 1
    }' \
-s <http://localhost:8000/api/v1/epic-custom-attributes>
When the creation is successful, the HTTP response is a 201 Created and the response body is a JSON epic custom attribute detail object

16.3. Get
To get an epic custom attribute send a GET request specifying the epic custom attribute id in the url

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epic-custom-attributes/14>
The HTTP response is a 200 OK and the response body is a JSON epic custom attribute detail object

16.4. Edit
To edit epic custom attributes send a PUT or a PATCH specifying the epic custom attribute id in the url. In a PATCH request you just need to send the modified data, in a PUT one the whole object must be sent.

curl -X PATCH \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "name": "Duration 1"
    }' \
-s <http://localhost:8000/api/v1/epic-custom-attributes/14>
When the update is successful, the HTTP response is a 200 OK and the response body is a JSON epic custom attribute detail object

16.5. Delete
To delete epic custom attributes send a DELETE specifying the epic custom attribute id in the url

curl -X DELETE \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epic-custom-attributes/14>
When delete succeeded, the HTTP response is a 204 NO CONTENT with an empty body response

16.6. Bulk update order
To update the order of multiple epic custom attributes at the same time send a POST request with the following data:

project (required)

bulk_epic_custom_attributes: list where each element is a list, the first element is the custom attribute id and the second the new order

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "bulk_epic_custom_attributes": [
            [
                14,
                10
            ],
            [
                13,
                15
            ]
        ],
        "project": 1
    }' \
-s <http://localhost:8000/api/v1/epic-custom-attributes/bulk_update_order>
When the update is successful, the HTTP response is a 204 NO CONTENT with an empty body response

1. Epic custom attributes values
17.1. Get
To get an epic custom attribute value send a GET request specifying the epic custom attribute id in the url

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/epics/custom-attributes-values/15>
The HTTP response is a 200 OK and the response body is a JSON epic custom attribute detail object

17.2. Edit
To edit epic custom attributes values send a PUT or a PATCH specifying the epic id in the url. "attribute_values" must be a JSON object with pairs epic custom atribute id - value. In a PATCH request you just need to send the modified data, in a PUT one the whole object must be sent.

curl -X PATCH \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "attributes_values": {
            "14": "240 min"
        },
        "version": 1
    }' \
-s <http://localhost:8000/api/v1/epics/custom-attributes-values/15>
When the update is successful, the HTTP response is a 200 OK and the response body is a JSON epic custom attribute detail object
