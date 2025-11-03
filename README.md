#  Okta Identity & Access Management (IAM) Demo

### Secure Authentication using FastAPI + Okta OAuth2 + OpenID Connect

![Okta Demo Screenshot](/OktaIAM-Integration*10_23_2025/OktaIAM-Integration/images/Screenshot%202025-10-23%20at%203.23.47 PM.png)
\_A simple demo showing Okta-hosted login integration with FastAPI backend.*

---

###  Overview

This project demonstrates how to build a **secure authentication flow** using **Okta’s Identity & Access Management (IAM)** platform integrated with a **Python FastAPI backend** and a **lightweight frontend** web interface.

It mirrors how real organizations implement:

-  **Single Sign-On (SSO)** via OAuth2 + OpenID Connect
-  **Secure redirect and token exchange**
-  **Protected application zones** (role-based access)
-  **Environment-based configuration**
-  **Modular backend routes and scalable architecture**

---

###  Why This Project Matters

Modern companies — from startups to global enterprises — rely on **Identity & Access Management** to control _who accesses what, when, and how_.

This demo models key enterprise IAM concepts in a simple, visual way:

| Core IAM Concept                        | Demonstrated Implementation                                      |
| --------------------------------------- | ---------------------------------------------------------------- |
| **Authentication & Authorization Flow** | OAuth2 / OpenID Connect integration with Okta                    |
| **Identity Federation**                 | Trust established between FastAPI app and Okta identity provider |
| **Least Privilege Access**              | Only authenticated users can reach `/secure/dashboard.html`      |
| **Separation of Concerns**              | Backend handles token exchange; frontend manages UI              |
| **Scalability & Extensibility**         | Structure reflects real enterprise microservice layouts          |

By completing this project, you demonstrate practical IAM understanding — the same security patterns used by **AWS**, **Microsoft**, and **Deloitte** to protect enterprise systems.

---

###  Key Learning Outcomes

- Implemented **OAuth2 Authorization Code Flow** with Okta
- Configured secure environment variables via `.env`
- Structured backend routes following **microservice best practices**
- Understood the flow of **identity federation** and **token exchange**
- Built a foundation for **Role-Based Access Control (RBAC)** and **MFA**

---

###  Project Preview

####  Okta Hosted Sign-In

When a user clicks **“Login with Okta”**, they are securely redirected to Okta’s hosted authentication page.

####  Successful Login → Redirect

After authentication, Okta returns an authorization code to the backend, which exchanges it for `id_token` and `access_token` — granting access to the secure dashboard.

---

###  Project Structure

```
OktaIAM-Integration/
│
├── backend/
│ ├── app.py
│ ├── routes/
│ │ └── okta_IAM.py
│ └── env_example.txt
│
├── frontend/
│ ├── index.html
│ └── secure/
│ ├── login.html
│ ├── index.html
│ └── dashboard.html
│
├── images/
│ └── okta-login.png
│
├── LICENSE
└── README.md
```

---

### ⚙️ How It Works

1️ **User Initiates Login**  
Frontend (`index.html`) → `/api/okta/login` → Redirects to Okta’s hosted sign-in page.

2️ **Okta Authenticates User**  
Okta validates credentials (and MFA if enabled).

3️ **Token Exchange**  
Upon success, Okta redirects to `/api/okta/callback`.  
The backend exchanges the authorization code for an **ID Token** and **Access Token**.

4️ **Access Granted**  
User is redirected to `/secure/dashboard.html`, representing a protected area accessible only after successful login.

---

###  Technologies Used

| Layer            | Technology                        |
| ---------------- | --------------------------------- |
| **Frontend**     | HTML5, CSS3, Vanilla JavaScript   |
| **Backend**      | Python 3.12 + FastAPI             |
| **IAM Provider** | Okta (OAuth 2.0 + OpenID Connect) |
| **Auth Flow**    | Authorization Code Flow           |
| **Config**       | `.env` environment-based secrets  |

---

###  Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/OktaIAM-Integration.git
   cd OktaIAM-Integration/backend
   ```

### 2. Install dependencies

pip install fastapi uvicorn requests python-dotenv

### 3. Create .env file

OKTA_CLIENT_ID=your_okta_client_id
OKTA_CLIENT_SECRET=your_okta_client_secret
OKTA_ISSUER_URL=https://yourorg.okta.com/oauth2/default
OKTA_REDIRECT_URI=http://localhost:8000/api/okta/callback

### 4. uvicorn backend.app:app --reload

### 5. Open in browser

Visit: http://localhost:8000

Click Login with Okta

Authenticate and view /secure/dashboard.html

 Future Enhancements

Add JWT validation middleware for backend token checks

Implement Role-Based Access Control (RBAC)

Integrate Multi-Factor Authentication (MFA)

Containerize via Docker for cloud deployment

Extend to Azure AD / Auth0 for cross-platform IAM demos

 Professional Value

This project demonstrates industry-relevant IAM skills and architectural design principles used in cybersecurity and cloud engineering.
It shows you understand how to bridge secure identity systems with backend APIs — a foundational skill for:

Identity & Access Management Analysts

Cloud Security Engineers

DevSecOps Specialists

Zero-Trust Architects

Author

Developed by: Abdalla Osman
