# Auth API documentation

## 3. Auth

### 3.1. Normal login

To login a user send a POST request containing the following data:

- type: "normal"
- username (required): this field also supports the user email
- password (required)

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{
    "password": "password",
    "type": "normal",
    "username": "test-username"
}' \
-s http://localhost:8000/api/v1/auth
```

When the login is successful, the HTTP response is a 200 OK and the response body is a JSON user auth detail object.

### 3.2. Github login

To login a user via GitHub send a POST request containing the following data:

- type: "github"
- code (required): your github authentication code
- token (optional): generated when creating a project’s membership (for accept invitations to projects)

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
      "type": "github",
      "code": "'${GITHUB_CODE}'"
  }' \
  https://api.taiga.io/api/v1/auth
```

When the login is successful, the HTTP response is a 200 OK and the response body is a JSON user auth detail object.

**Get GitHub authorized code:**
To get the GitHub code you have to follow the first step (Redirect users to request GitHub access) described in GitHub Documentation for Developers - API - OAuth - Web Application Flow.

Taiga needs privileges to get the user email from Github so you have to use the scope `user:email`.

### 3.3. Refresh auth token

To refresh the auth token send a POST request containing the following data:

- refresh (required): the refresh token

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{
    "refresh": "<refresh_token>"
}' \
-s http://localhost:8000/api/v1/auth/refresh
```

When the refresh is successful, the HTTP response is a 200 OK and the response body is a JSON refresh token detail object.

### 3.4. Public registry

To register a user without invitation send a POST request containing the following data:

- type: "public"
- username (required)
- password (required)
- email (required)
- full_name (required)
- accepted_terms (required): boolean

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{
    "accepted_terms": "true",
    "email": "test-register2@email.com",
    "full_name": "test",
    "password": "password",
    "type": "public",
    "username": "test-username2"
}' \
-s http://localhost:8000/api/v1/auth/register
```

When the registration is successful, the HTTP response is a 201 CREATED and the response body is a JSON user auth detail object.

### 3.5. Private registry

To add a user into a project via invitation send a POST request containing the following data:

- type: "private"
- existing (required): indicates if the user is member or not
- token (required): generated when creating a project’s membership
- username (required)
- password (required)
- email (required only if the user doesn’t exist in the platform)
- full_name (required only if the user doesn’t exist in the platform)
- accepted_terms (required): boolean

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{
    "accepted_terms": "true",
    "email": "test-register@email.com",
    "existing": false,
    "full_name": "test",
    "password": "password",
    "token": "00000000-0000-0000-0000-000000000000",
    "type": "private",
    "username": "test-username"
}' \
-s http://localhost:8000/api/v1/auth/register
```

When the registration is successful, the HTTP response is a 201 CREATED and the response body is a JSON user auth detail object.