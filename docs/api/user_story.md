# User Stories API documentation

## 18. User stories

### 18.1. List

To list user stories send a GET request with the following parameters:

```bash
curl -X GET \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${AUTH_TOKEN}" \
    -s http://localhost:8000/api/v1/userstories
```

The HTTP response is a 200 OK and the response body is a JSON list of user story list objects

The results can be filtered using the following parameters:

- project: project id
- milestone: milestone id
- milestone__isnull: (true|false) if you are looking for user stories associated with a milestone or not
- status: status id

status__is_archived: (true|false)

tags: separated by ","

watchers: watching user id

assigned_to: assigned to user id

epic: epic id

role: role id

status__is_closed: (true|false)

exclude_status: status id

exclude_tags: separated by ","

exclude_assigned_to: assigned to user id

exclude role: role id

exclude epic: epic id

the "exclude_" params work excluding from the response the results with which they match.
curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/userstories?project=1>
18.2. Create
To create user stories send a POST request with the following data:

assigned_to: user id

backlog_order: order in the backlog

blocked_note: reason why the user story is blocked

client_requirement: boolean

description: string

is_blocked: boolean

is_closed: boolean

kanban_order: order in the kanban

milestone: milestone id

points: dictionary of points

project (required): project id

sprint_order: order in the milestone

status: status id

subject (required)

tags: array of strings

team_requirement: boolean

watchers: array of watcher id’s

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "assigned_to": null,
        "backlog_order": 2,
        "blocked_note": "blocking reason",
        "client_requirement": false,
        "description": "Implement API CALL",
        "is_blocked": false,
        "is_closed": true,
        "kanban_order": 37,
        "milestone": null,
        "points": {
            "1": 4,
            "2": 3,
            "3": 2,
            "4": 1
        },
        "project": 1,
        "sprint_order": 2,
        "status": 2,
        "subject": "Customer personal data",
        "tags": [
            "service catalog",
            "customer"
        ],
        "team_requirement": false,
        "watchers": []
    }' \
-s http://localhost:8000/api/v1/userstories
curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "project": 1,
        "subject": "Customer personal data"
    }' \
-s <http://localhost:8000/api/v1/userstories>
When the creation is successful, the HTTP response is a 201 Created and the response body is a JSON user story detail object

18.3. Get
To get a user story send a GET request specifying the user story id in the url

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/userstories/1>
The HTTP response is a 200 OK and the response body is a JSON user story detail (GET) object

18.4. Get by ref
To get a user story send a GET request specifying the user story reference and one of the following parameters:

project (project id)

project__slug

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/userstories/by_ref?ref=1\&project=1>
The HTTP response is a 200 OK and the response body is a JSON user story detail (GET) object

18.5. Edit
To edit user stories send a PUT or a PATCH specifying the user story id in the url. In a PATCH request you just need to send the modified data, in a PUT one the whole object must be sent.

curl -X PATCH \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "subject": "Patching subject",
        "version": 1
    }' \
-s <http://localhost:8000/api/v1/userstories/1>
When the creation is successful, the HTTP response is a 200 OK and the response body is a JSON user story detail object

18.6. Delete
To delete user stories send a DELETE specifying the user story id in the url

curl -X DELETE \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/userstories/1>
When delete succeeded, the HTTP response is a 204 NO CONTENT with an empty body response

18.7. Bulk creation
To create multiple user stories at the same time send a POST request with the following data:

project_id (required)

status_id

bulk_stories: user story subjects, one per line

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "bulk_stories": "US 1 \n US 2 \n US 3",
        "project_id": 1
    }' \
-s <http://localhost:8000/api/v1/userstories/bulk_create>
When the creation is successful, the HTTP response is a 200 OK and the response body is a JSON list of user story detail object

18.8. Bulk update backlog order
To update the backlog order of multiple user stories at the same time send a POST request with the following data:

project_id (required)

bulk_stories: list where each element is a json object with two attributes, the user story id and the new order

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "bulk_stories": [
            {
                "order": 10,
                "us_id": 1
            },
            {
                "order": 15,
                "us_id": 2
            }
        ],
        "project_id": 1
    }' \
-s <http://localhost:8000/api/v1/userstories/bulk_update_backlog_order>
When the update is successful, the HTTP response is a 200 OK and the response body is a JSON list of user story detail object

18.9. Bulk update kanban order
To update the kanban order of multiple user stories at the same time send a POST request with the following data:

project_id (required)

bulk_stories: list where each element is a json object with two attributes, the user story id and the new order

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "bulk_stories": [
            {
                "order": 10,
                "us_id": 1
            },
            {
                "order": 15,
                "us_id": 2
            }
        ],
        "project_id": 1
    }' \
-s <http://localhost:8000/api/v1/userstories/bulk_update_kanban_order>
When the update is successful, the HTTP response is a 200 OK and the response body is a JSON list of user story detail object

18.10. Bulk update sprint order
To update the sprint order of multiple user stories at the same time send a POST request with the following data:

project_id (required)

bulk_stories: list where each element is a json object with two attributes, the user story id and the new order

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "bulk_stories": [
            {
                "order": 10,
                "us_id": 1
            },
            {
                "order": 15,
                "us_id": 2
            }
        ],
        "project_id": 1
    }' \
-s <http://localhost:8000/api/v1/userstories/bulk_update_sprint_order>
When the update is successful, the HTTP response is a 200 OK and the response body is a JSON list of user story detail object

18.11. Bulk update milestone
To update the sprint of multiple user stories at the same time send a POST request with the following data:

project_id (required)

milestone_id (required)

bulk_stories: list where each element is a json object with two attributes, the user story id and the new order

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "bulk_stories": [
            {
                "order": 10,
                "us_id": 1
            },
            {
                "order": 15,
                "us_id": 2
            }
        ],
        "milestone_id": 1,
        "project_id": 1
    }' \
-s <http://localhost:8000/api/v1/userstories/bulk_update_milestone>
When the update is successful, the HTTP response is a 204 NO CONTENT with an empty body response

18.12. Filters data
To get the user stories filters data send a GET request specifying the project id in the url

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/userstories/filters_data?project=1>
The HTTP response is a 200 OK and the response body is a JSON user story filters data object

18.13. Vote a user story
To add a vote to a user story send a POST request specifying the user story id in the url

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/userstories/1/upvote>
The HTTP response is a 200 OK with an empty body response

18.14. Remove vote from a user story
To remove a vote from a user story send a POST request specifying the user story id in the url

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/userstories/1/downvote>
When remove of the vote succeeded, the HTTP response is a 200 OK with an empty body response

18.15. Get user story voters list
To get the list of voters from a user story send a GET request specifying the user story id in the url

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/userstories/2/voters>
The HTTP response is a 200 OK and the response body is a JSON list of user story voter object

18.16. Watch a user story
To watch a user story send a POST request specifying the project id in the url

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/userstories/1/watch>
The HTTP response is a 200 OK with an empty body response

18.17. Stop watching a user story
To stop watching a user story send a POST request specifying the user story id in the url

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/userstories/1/unwatch>
The HTTP response is a 200 OK with an empty body response

18.18. List user story watchers
To get the list of watchers from a user story send a GET request specifying the user story id in the url

{
    "full_name": "Vanesa Torres",
    "id": 6,
    "username": "user2114747470430251528"
}
The HTTP response is a 200 OK and the response body is a JSON list of user story watcher object

18.19. List attachments
To list user story attachments send a GET request with the following parameters:

project: project id

object_id: user story id

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/userstories/attachments?object_id=1\&project=1>
The HTTP response is a 200 OK and the response body is a JSON list of attachment detail objects

18.20. Create attachment
To create user story attachments send a POST request with the following data:

object_id (required): user story id

project (required): project id

attached_file (required): attaching file

description

is_deprecated

curl -X POST \
-H "Content-Type: multipart/form-data" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-F attached_file=@test.png \
-F from_comment=False \
-F object_id=1 \
-F project=1 \
-s <http://localhost:8000/api/v1/userstories/attachments>
When the creation is successful, the HTTP response is a 201 Created and the response body is a JSON attachment detail object

18.21. Get attachment
To get a user story attachment send a GET request specifying the user story attachment id in the url

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/userstories/attachments/415>
The HTTP response is a 200 OK and the response body is a JSON attachment detail object

18.22. Edit attachment
To edit user story attachments send a PUT or a PATCH specifying the user story attachment id in the url. In a PATCH request you just need to send the modified data, in a PUT one the whole object must be sent.

curl -X PATCH \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "description": "patching description"
    }' \
-s <http://localhost:8000/api/v1/userstories/attachments/1>
When the creation is successful, the HTTP response is a 200 OK and the response body is a JSON attachment detail object

18.23. Delete attachment
To delete user story attachments send a DELETE specifying the user story attachment id in the url

curl -X DELETE \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/userstories/attachments/458>
When delete succeeded, the HTTP response is a 204 NO CONTENT with an empty body response

1. User story status
19.1. List
To list user story status send a GET request with the following parameters:

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/userstory-statuses>
The HTTP response is a 200 OK and the response body is a JSON list of user story status detail objects

The results can be filtered using the following parameters:

project: project id

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/userstory-statuses?project=1>
19.2. Create
To create user story statuses send a POST request with the following data:

color: in hexadecimal

is_closed: (true|false)

name (required)

order: integer

project: (required): project id

wip_limit: integer representing the max number of user stories in this status

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "color": "#AAAAAA",
        "is_closed": true,
        "name": "New status",
        "order": 8,
        "project": 1,
        "wip_limit": 6
    }' \
-s http://localhost:8000/api/v1/userstory-statuses
curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "name": "New status name",
        "project": 1
    }' \
-s <http://localhost:8000/api/v1/userstory-statuses>
When the creation is successful, the HTTP response is a 201 Created and the response body is a JSON user story status detail object

19.3. Get
To get a user story status send a GET request specifying the user story status id in the url

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/userstory-statuses/1>
The HTTP response is a 200 OK and the response body is a JSON user story status detail object

19.4. Edit
To edit user story statuses send a PUT or a PATCH specifying the user story status id in the url. In a PATCH request you just need to send the modified data, in a PUT one the whole object must be sent.

curl -X PATCH \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "name": "Patch status name"
    }' \
-s <http://localhost:8000/api/v1/userstory-statuses/1>
When the creation is successful, the HTTP response is a 200 OK and the response body is a JSON user story status detail object

19.5. Delete
To delete user story satuses send a DELETE specifying the user story status id in the url

curl -X DELETE \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s <http://localhost:8000/api/v1/userstory-statuses/1>
When delete succeeded, the HTTP response is a 204 NO CONTENT with an empty body response

19.6. Bulk update order
To update the order of multiple user story statues at the same time send a POST request with the following data:

project (required)

bulk_userstory_statuses: list where each element is a list, the first element is the status id and the second the new order

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-d '{
        "bulk_userstory_statuses": [
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
-s <http://localhost:8000/api/v1/userstory-statuses/bulk_update_order>
When the update is successful, the HTTP response is a 204 NO CONTENT with an empty body response
