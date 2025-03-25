INSERT INTO questions (question_text, question_type, correct_answer) VALUES
('What is the primary difference between an insider threat and a shadow IT threat actor?', 'multiple_choice', 'C'),
('An application creates a temporary file to save a value for later use. A malicious actor deletes this file after its created but before its subsequent use by the application. What type of vulnerability is being exploited in this situation?', 'multiple_choice', 'B'),
('During the decommissioning process of a database server, the IT department of Dion Training ensures that all stored customer data is rendered unrecoverable to protect against unauthorized access in the future. Which of the following practices is the IT department employing in this scenario?', 'multiple_choice', 'C'),
('Which of the following terms BEST describes a situation in which a company avoids addressing known system inefficiencies or shortcuts due to time constraints, potentially leading to future rework and vulnerabilities?', 'multiple_choice', 'D'),
('Dion Training Solutions is implementing a security system for its research facility, where sensitive data is stored. If the access control system fails, which mode should be adopted to ensure that no unauthorized personnel can enter the facility, even if it means some inconvenience to authorized staff?', 'multiple_choice', 'B'),
('You are a cybersecurity analyst for a large enterprise that has experienced several security incidents resulting from insider threats and compromised user accounts. The organization wants to enhance its security posture by implementing User Behavior Analytics (UBA). Which of the following approaches would be the MOST effective way to implement UBA for the given scenario?', 'multiple_choice', 'C'),
('Kelly Innovations decides to manage its IT infrastructure within its physical location, retaining full control over its hardware, software, and data. Which of the following security implications is MOST directly associated with this approach?', 'multiple_choice', 'C'),
('Kelly Innovations LLC is implementing a wireless network and needs a wireless authentication method that support multiple mechanisms for authenticating both wired and wireless users. Which protocol BEST fits their requirements?', 'multiple_choice', 'D'),
('Dion Training is implementing a security device tasked with inspecting live network traffic and taking immediate action to mitigate potential threats. Which of the following security items would MOST effectively satisfy this requirement?', 'multiple_choice', 'B'),
('Jenny, a newly hired sales representative, has been granted access to view customer records but is unable to modify, delete or add new ones. Only managers and the IT department have the ability to make changes to these records to maintain data integrity. Which principle is the organization applying?', 'multiple_choice', 'B');


INSERT INTO options (question_id, option_letter, option_text) VALUES (1, 'A', 'Level of sophistication/capability');
INSERT INTO options (question_id, option_letter, option_text) VALUES (1, 'B', 'Resources/funding');
INSERT INTO options (question_id, option_letter, option_text) VALUES (1, 'C', 'Malicious intent');
INSERT INTO options (question_id, option_letter, option_text) VALUES (1, 'D', 'Level of access');
INSERT INTO options (question_id, option_letter, option_text) VALUES (2, 'A', 'Race conditions');
INSERT INTO options (question_id, option_letter, option_text) VALUES (2, 'B', 'Time-of-use(TOU)');
INSERT INTO options (question_id, option_letter, option_text) VALUES (2, 'C', 'Memory leaks');
INSERT INTO options (question_id, option_letter, option_text) VALUES (2, 'D', 'Memory injection');
INSERT INTO options (question_id, option_letter, option_text) VALUES (3, 'A', 'Assignment');
INSERT INTO options (question_id, option_letter, option_text) VALUES (3, 'B', 'Enumeration');
INSERT INTO options (question_id, option_letter, option_text) VALUES (3, 'C', 'Sanitization');
INSERT INTO options (question_id, option_letter, option_text) VALUES (3, 'D', 'Inventory');
INSERT INTO options (question_id, option_letter, option_text) VALUES (4, 'A', 'Complexity');
INSERT INTO options (question_id, option_letter, option_text) VALUES (4, 'B', 'Cost');
INSERT INTO options (question_id, option_letter, option_text) VALUES (4, 'C', 'Single point of failure');
INSERT INTO options (question_id, option_letter, option_text) VALUES (4, 'D', 'Technical debt');
INSERT INTO options (question_id, option_letter, option_text) VALUES (5, 'A', 'Rate-based filtering');
INSERT INTO options (question_id, option_letter, option_text) VALUES (5, 'B', 'Fail-closed');
INSERT INTO options (question_id, option_letter, option_text) VALUES (5, 'C', 'Passive mode');
INSERT INTO options (question_id, option_letter, option_text) VALUES (5, 'D', 'Fail-open');
INSERT INTO options (question_id, option_letter, option_text) VALUES (6, 'A', 'Using UBA to monitor and analyze the activities of privileged users with elevated access rights only');
INSERT INTO options (question_id, option_letter, option_text) VALUES (6, 'B', 'Implementing UBA on the organization''s perimeter firewalls to analyze incoming and outgoing network traffic');
INSERT INTO options (question_id, option_letter, option_text) VALUES (6, 'C', 'Deploying UBA on all endpoint devices to monitor user interactions and application usage');
INSERT INTO options (question_id, option_letter, option_text) VALUES (6, 'D', 'Configuring UBA to perform scheduled scans of all user accounts prevent any anomalies');
INSERT INTO options (question_id, option_letter, option_text) VALUES (7, 'A', 'Dependence on external patch availability');
INSERT INTO options (question_id, option_letter, option_text) VALUES (7, 'B', 'Risk transference to third-party vendors');
INSERT INTO options (question_id, option_letter, option_text) VALUES (7, 'C', 'Increased responsibility for physical security');
INSERT INTO options (question_id, option_letter, option_text) VALUES (7, 'D', 'Multi-tenancy risks');
INSERT INTO options (question_id, option_letter, option_text) VALUES (8, 'A', 'RADIUS');
INSERT INTO options (question_id, option_letter, option_text) VALUES (8, 'B', 'WPA3');
INSERT INTO options (question_id, option_letter, option_text) VALUES (8, 'C', 'LDAP');
INSERT INTO options (question_id, option_letter, option_text) VALUES (8, 'D', 'EAP');
INSERT INTO options (question_id, option_letter, option_text) VALUES (9, 'A', 'Fail-open mode');
INSERT INTO options (question_id, option_letter, option_text) VALUES (9, 'B', 'An active device');
INSERT INTO options (question_id, option_letter, option_text) VALUES (9, 'C', 'Fail-closed mode');
INSERT INTO options (question_id, option_letter, option_text) VALUES (9, 'D', 'A passive device');
INSERT INTO options (question_id, option_letter, option_text) VALUES (10, 'A', 'Attribute-based access control (ABAC)');
INSERT INTO options (question_id, option_letter, option_text) VALUES (10, 'B', 'Principle of least privilege');
INSERT INTO options (question_id, option_letter, option_text) VALUES (10, 'C', 'Mandatory access control (MAC)');
INSERT INTO options (question_id, option_letter, option_text) VALUES (10, 'D', 'Data classification');
