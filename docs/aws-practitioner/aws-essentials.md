# Notes from AWS Cloud Practitioner Essentials

## Client-Server Model:
The client–server model is a distributed application structure that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients [wiki].

## How the Browser Interacts With the Servers? [[see](https://www.geeksforgeeks.org/client-server-model/)]


When a user tries to access a website or file, several steps occur in the background to fetch and display the content:

   1. The user enters a URL (Uniform Resource Locator) into their web browser. This prompts the browser to send a request to the DNS (Domain Name System) server to locate the corresponding web server.
   2. The DNS server searches for the IP address linked to the requested domain.
   3. Once found, the DNS server returns the web server’s IP address to the browser.
   4. The browser then sends an HTTP/HTTPS request to the identified web server’s IP address.
   5. The web server processes the request and responds by sending the required files (such as HTML, CSS, JavaScript, and media files) back to the browser.
   6. The browser interprets these files and constructs the webpage using various components:
      *  DOM (Document Object Model) interpreter for structuring the page.
      *  CSS interpreter for styling and layout.
      *  JavaScript engine for dynamic interactions.
      *  These are optimized by JIT (Just-In-Time) compilation for better performance.
    7. Finally, the fully rendered website is displayed to the user.

## Advantages and Disadvantages of the Client-Server Model
**Advantages:**

- Centralized Management: All data and resources are stored in a single location, making it easier to manage and secure.
- Cost Efficiency: Requires lower maintenance costs compared to distributed systems, and data recovery is more feasible.
- Scalability: The client and server can be upgraded independently, allowing for flexible system expansion.

**Disadvantages:**

- Security Risks: If the server is compromised, clients can be infected with viruses, Trojans, or worms.
- Vulnerability to Attacks: Servers are susceptible to Denial of Service (DoS) attacks, which can disrupt access.
- Data Integrity Risks: Information transmitted between the client and server can be spoofed, intercepted, or altered by attackers.
- Phishing & MITM Attacks: Hackers can steal login credentials or sensitive data through Man-in-the-Middle (MITM) attacks or phishing schemes.


## Deployment Models for Cloud Computing:
1. cloud-based:
    - Run all parts of the application in the cloud.
    - Migrate existing applications to the cloud.
    - Design and build new applications in the cloud.
2. on-premises:
    - Deploy resources by using virtualization and resource management tools.
    - Increase resource utilization by using application management and virtualization technologies.
3. hybrid:
    - Connect cloud-based resources to on-premises infrastructure.
    - Integrate cloud-based resources with legacy IT applications.
    
### Benefits of Cloud Computing:
1. Pay for what you use!
2. Pay when you use!
3. No need to `alloc` or `malloc`!
4. Use more, pay less!
5. Speed up as you in run!
6. Be Marco Polo!
