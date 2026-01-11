-- Seed data for Quiz Application
-- Auto-generated from quiz.json

-- Clear existing data
DELETE FROM correct_answers;
DELETE FROM options;
DELETE FROM questions;
DELETE FROM subjects;

-- Reset sequences
ALTER SEQUENCE subjects_id_seq RESTART WITH 1;
ALTER SEQUENCE questions_id_seq RESTART WITH 1;
ALTER SEQUENCE options_id_seq RESTART WITH 1;
ALTER SEQUENCE correct_answers_id_seq RESTART WITH 1;

-- Insert subjects
INSERT INTO subjects (name, description) VALUES
('Security+', 'CompTIA Security+ certification exam preparation questions');

-- Question 1
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'What is the primary difference between an insider threat and a shadow IT threat actor?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(1, 'A', 'Level of sophistication/capability'),
(1, 'B', 'Resources/funding'),
(1, 'C', 'Malicious intent'),
(1, 'D', 'Level of access');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(1, 'C');

-- Question 2
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'An application creates a temporary file to save a value for later use. A malicious actor deletes this file after its created but before its subsequent use by the application. What type of vulnerability is being exploited in this situation?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(2, 'A', 'Race conditions'),
(2, 'B', 'Time-of-use(TOU)'),
(2, 'C', 'Memory leaks'),
(2, 'D', 'Memory injection');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(2, 'B');

-- Question 3
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'During the decommissioning process of a database server, the IT department of Dion Training ensures that all stored customer data is rendered unrecoverable to protect against unauthorized access in the future. Which of the following practices is the IT department employing in this scenario?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(3, 'A', 'Assignment'),
(3, 'B', 'Enumeration'),
(3, 'C', 'Sanitization'),
(3, 'D', 'Inventory');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(3, 'C');

-- Question 4
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which of the following terms BEST describes a situation in which a company avoids addressing known system inefficiencies or shortcuts due to time constraints, potentially leading to future rework and vulnerabilities?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(4, 'A', 'Complexity'),
(4, 'B', 'Cost'),
(4, 'C', 'Single point of failure'),
(4, 'D', 'Technical debt');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(4, 'D');

-- Question 5
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Dion Training Solutions is implementing a security system for its research facility, where sensitive data is stored. If the access control system fails, which mode should be adopted to ensure that no unauthorized personnel can enter the facility, even if it means some inconvenience to authorized staff?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(5, 'A', 'Rate-based filtering'),
(5, 'B', 'Fail-closed'),
(5, 'C', 'Passive mode'),
(5, 'D', 'Fail-open');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(5, 'B');

-- Question 6
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'You are a cybersecurity analyst for a large enterprise that has experienced several security incidents resulting from insider threats and compromised user accounts. The organization wants to enhance its security posture by implementing User Behavior Analytics (UBA). Which of the following approaches would be the MOST effective way to implement UBA for the given scenario?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(6, 'A', 'Using UBA to monitor and analyze the activities of privileged users with elevated access rights only'),
(6, 'B', 'Implementing UBA on the organization''s perimeter firewalls to analyze incoming and outgoing network traffic'),
(6, 'C', 'Deploying UBA on all endpoint devices to monitor user interactions and application usage'),
(6, 'D', 'Configuring UBA to perform scheduled scans of all user accounts prevent any anomalies');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(6, 'C');

-- Question 7
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Kelly Innovations decides to manage its IT infrastructure within its physical location, retaining full control over its hardware, software, and data. Which of the following security implications is MOST directly associated with this approach?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(7, 'A', 'Dependence on external patch availability'),
(7, 'B', 'Risk transference to third-party vendors'),
(7, 'C', 'Increased responsibility for physical security'),
(7, 'D', 'Multi-tenancy risks');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(7, 'C');

-- Question 8
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Kelly Innovations LLC is implementing a wireless network and needs a wireless authentication method that support multiple mechanisms for authenticating both wired and wireless users. Which protocol BEST fits their requirements?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(8, 'A', 'RADIUS'),
(8, 'B', 'WPA3'),
(8, 'C', 'LDAP'),
(8, 'D', 'EAP');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(8, 'D');

-- Question 9
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Dion Training is implementing a security device tasked with inspecting live network traffic and taking immediate action to mitigate potential threats. Which of the following security items would MOST effectively satisfy this requirement?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(9, 'A', 'Fail-open mode'),
(9, 'B', 'An active device'),
(9, 'C', 'Fail-closed mode'),
(9, 'D', 'A passive device');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(9, 'B');

-- Question 10
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Jenny, a newly hired sales representative, has been granted access to view customer records but is unable to modify, delete or add new ones. Only managers and the IT department have the ability to make changes to these records to maintain data integrity. Which principle is the organization applying?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(10, 'A', 'Attribute-based access control (ABAC)'),
(10, 'B', 'Principle of least privilege'),
(10, 'C', 'Mandatory access control (MAC)'),
(10, 'D', 'Data classification');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(10, 'B');

-- Question 11
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Reed is getting a new computer from his employer, Kelly Innovations LLC. He wants to remove all his personal data from his old computer, ensuring it''s irretrievable. Which of the following methods should he use?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(11, 'A', 'System restore'),
(11, 'B', 'Disk defragmentation'),
(11, 'C', 'Secure erase'),
(11, 'D', 'Emptying the recycle bin');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(11, 'C');

-- Question 12
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'After the IT department proposed a new software update, Kevin, a system analyst, evaluates the potential effects of this change on the system performance, user experience, and business processes. Which term BEST describes Kevin''s evaluation?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(12, 'A', 'Version control'),
(12, 'B', 'Approval process'),
(12, 'C', 'Backout plan'),
(12, 'D', 'Impact analysis');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(12, 'D');

-- Question 13
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'A company''s access control mechanism determines access to resources base on user''s job functions. The system enforces access control based on these predefined responsibilities, and users do not have the discretion to modify or override access permissions. Which type of access control mechanism is being used in this scenario?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(13, 'A', 'Discretionary'),
(13, 'B', 'Rule-based'),
(13, 'C', 'Attribute-based'),
(13, 'D', 'Role-based');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(13, 'D');

-- Question 14
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'A software development company regularly releases software updates to its global customer base. Recently, some customers reported receiving unauthorized and potentially malicious software updates. The company is now seeking to implement a security technique to ensure the authenticity and integrity of its software updates when delivered to customers. Which of the following would BEST assist in achieving this goal?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(14, 'A', 'Antivirus scanning'),
(14, 'B', 'IDS solution'),
(14, 'C', 'MFA'),
(14, 'D', 'Code signing');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(14, 'D');

-- Question 15
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which of the following terms BEST describes the measurement used to describe a 7% possibility of hardware failure in the next year based on past statistical data?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(15, 'A', 'Exposure factor'),
(15, 'B', 'Severity ranking'),
(15, 'C', 'Probability'),
(15, 'D', 'Likelihood');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(15, 'C');

-- Question 16
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which of the following mitigation techniques inspects and controls incoming and outgoing network traffic on a per-application basis?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(16, 'A', 'Intrusion Detection System'),
(16, 'B', 'Network Segmentation'),
(16, 'C', 'Host-based Firewall'),
(16, 'D', 'Data Loss Prevention');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(16, 'C');

-- Question 17
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'At Kelly Innovations LLC, Sasha received an unexpected call from someone claiming to be from the IT department. The caller asked her to confirm her username and password for a system upgrade. Unsure, Sasha hesitated and asked the caller to provide some form of identification or a callback number. Which of the following terms describes the Social Engineering technique that Sasha encountered?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(17, 'A', 'Vishing'),
(17, 'B', 'Pharming'),
(17, 'C', 'Vulnerability Assessment'),
(17, 'D', 'Smishing');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(17, 'A');

-- Question 18
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Emily is part of the IT team and oversees the secure transmission of sensitive data within her organization, ensuring that all systems comply with integrity protocols. She monitors for any inconsistencies or issues that could compromise data integrity. What role does Emily most likely hold?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(18, 'A', 'Data Custodian'),
(18, 'B', 'Data Controller'),
(18, 'C', 'Data Processor'),
(18, 'D', 'Data Owner');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(18, 'A');

-- Question 19
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'If a company''s server has an estimated Single Loss Expectancy (SLE) of $15,000 due to an operational failure, and the Annual Rate of Occurrence (ARO) of these failures is expected to be 0.1 times per year, what is the Annual Loss Expectancy (ALE)?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(19, 'A', '$150,000'),
(19, 'B', '$150'),
(19, 'C', '$15,000'),
(19, 'D', '$1,500');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(19, 'D');

-- Question 20
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Trust Us is a company that acts as a trusted entity. They issue and manage security credentials and issue digital signature wrappers for public keys for message encryption. What type of company is Trust Us?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(20, 'A', 'Root of Trust'),
(20, 'B', 'Registration Authority'),
(20, 'C', 'Blockchain'),
(20, 'D', 'Certificate Authority');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(20, 'D');

-- Question 21
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'When considering data storage, which of the following BEST describes a method to capture the state of a system at a specific point in time, offering a quick recovery solution without the need for a full backup?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(21, 'A', 'Snapshots'),
(21, 'B', 'Full backups'),
(21, 'C', 'Differential backups'),
(21, 'D', 'Incremental backups');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(21, 'A');

-- Question 22
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Dion Training wants to increase the trustworthiness of its website for its clients. They are seeking a certificate that is signed and verified by a recognized external authority. What type of certificate should they pursue?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(22, 'A', 'Wildcard certificate'),
(22, 'B', 'Self-signed certificate'),
(22, 'C', 'Third-party certificate'),
(22, 'D', 'CSR');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(22, 'C');

-- Question 23
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which of the following mitigation techniques can help reduce the exposure of systems to potential attacks by turning off unneeded or unwanted network communication channels?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(23, 'A', 'Disabling ports and protocols'),
(23, 'B', 'Changing Default Passwords'),
(23, 'C', 'Patching'),
(23, 'D', 'Removing unnecessary software');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(23, 'A');

-- Question 24
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'A newly established e-commerce platform needs to identify potential risks to its operations. What should be their first step in the risk management process?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(24, 'A', 'Conducting a Business Impact Analysis'),
(24, 'B', 'Setting up a Risk Register'),
(24, 'C', 'Performing Risk Identification'),
(24, 'D', 'Developing Risk Management Strategies');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(24, 'C');

-- Question 25
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'A small business is establishing a risk management process and wants to record and monitor identified risks. What tool should they prioritize setting up?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(25, 'A', 'Risk Register'),
(25, 'B', 'Business Impact Analysis Report'),
(25, 'C', 'Risk Tolerance Policy'),
(25, 'D', 'Risk Appetite Statement');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(25, 'A');

-- Question 26
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'A software development firm needs to decide how to handle the risk of potential litigation due to copyright infringement. Which risk management strategy would be most appropriate?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(26, 'A', 'Risk Acceptance'),
(26, 'B', 'Risk Avoidance'),
(26, 'C', 'Risk Transfer'),
(26, 'D', 'Risk Mitigation');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(26, 'C');

-- Question 27
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'An online retailer is conducting a Business Impact Analysis. What are they likely focusing on to ensure business continuity?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(27, 'A', 'Recovery Time Objective (RTO) and Recovery Point Objective (RPO)'),
(27, 'B', 'Annualized Rate of Occurrence (ARO) and Probability'),
(27, 'C', 'Risk Tolerance and Risk Appetite'),
(27, 'D', 'Risk Register Updates');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(27, 'A');

-- Question 28
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'A cloud service provider is evaluating the potential impacts of various risks on their service availability. What method of risk analysis should they use to assess the potential frequency of these risks?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(28, 'A', 'Qualitative Risk Analysis'),
(28, 'B', 'Quantitative Risk Analysis'),
(28, 'C', 'Assessing the Annualized Rate of Occurrence (ARO)'),
(28, 'D', 'Conducting a Risk Tolerance Evaluation');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(28, 'C');

-- Question 29
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Dion Training is considering a collaboration with a new IT service vendor. To ensure compliance and adherence to industry standards, Dion Training wishes to see verifiable evaluations of the vendor''s security controls and practices. Which of the following would provide Dion Training with insights into the vendor''s own internal evaluations of their security measures?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(29, 'A', 'Customer testimonials'),
(29, 'B', 'External penetration test reports'),
(29, 'C', 'Regulatory compliance certificates'),
(29, 'D', 'Evidence of internal audits');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(29, 'D');

-- Question 30
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Rippled, a drink vendor, is developing a disaster recovery plan to ensure the swift recovery of critical systems and processes in the event of a disruption. They are defining a specific metric which is the amount of acceptable amount of time it will take to return to normal business. What measure are they defining?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(30, 'A', 'RTO'),
(30, 'B', 'MTBF'),
(30, 'C', 'MTTR'),
(30, 'D', 'RPO');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(30, 'A');

-- Question 31
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Kelly Innovations LLC has integrated a new payment gateway into their application. To ensure no potential security gaps exist, especially related to data breaches or financial data leaks, which of the following actions would be the MOST effective?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(31, 'A', 'Engaging penetration testers to mimic real-world hacking techniques'),
(31, 'B', 'Updating the application to its latest version post-integration'),
(31, 'C', 'Ensuring two-factor authentication is enabled for application users'),
(31, 'D', 'Deploying a new intrusion detection system for the payment module');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(31, 'A');

-- Question 32
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Jason and Reed, both IT specialists at Kelly Innovations LLC, are tasked with ensuring the workstations'' secure baseline remains uncompromised over time. Which technique would BEST help them achieve this?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(32, 'A', 'Implement playbooks to enforce and verify settings'),
(32, 'B', 'Rely solely on antivirus scans to detect changes in workstation configuration.'),
(32, 'C', 'Use Windows Update without a validation process'),
(32, 'D', 'Manually check each workstation at month-end for deviations from the baseline');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(32, 'A');

-- Question 33
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which email security standard helps prevent email spoofing by allowing domain owners to specify which mail servers are authorized to send email on their behalf?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(33, 'A', 'DKIM'),
(33, 'B', 'SPF'),
(33, 'C', 'DMARC'),
(33, 'D', 'SMTP');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(33, 'B');

-- Question 34
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which of the following terms refers to a major program executed by powerful entities to shift public opinion?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(34, 'A', 'Digital diplomacy'),
(34, 'B', 'Influence campaign'),
(34, 'C', 'Soft power'),
(34, 'D', 'Digital espionage');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(34, 'B');

-- Question 35
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Dion Training Solutions recently integrated a single security solution that provides multiple security functions at one point on their network. This solution incorporates functionalities such as intrusion prevention, gateway anti-virus, and VPN. Which of the following BEST describes this solution?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(35, 'A', 'UTM'),
(35, 'B', 'Firewall'),
(35, 'C', 'VPN gateway'),
(35, 'D', 'IPS');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(35, 'A');

-- Question 36
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which of the following mitigation techniques can help prevent users from making changes to the security features of devices by applying predefined security standards?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(36, 'A', 'Configuration enforcement'),
(36, 'B', 'Patching'),
(36, 'C', 'Encryption'),
(36, 'D', 'Least Privilege');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(36, 'A');

-- Question 37
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which of the following strategies is MOST effective for organizations aiming to mitigate the risk of widespread disruptions due to a localized issue in their infrastructure?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(37, 'A', 'Data masking'),
(37, 'B', 'Permission restrictions'),
(37, 'C', 'Geographic restrictions'),
(37, 'D', 'Infrastructure diversification');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(37, 'D');

-- Question 38
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'You are making an appointment to get your hair cut. When you enter your personal data into the website for Dye My Darling, the data is placed in a database and paired with a smaller set of symbols that will represent your data. To access your personal data, your stylists'' computer will access the database. If an attacker gains access to the computer, they will only see the set of symbols, not your personal data. What method of concealment is Dye My Darling using?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(38, 'A', 'Tokenization'),
(38, 'B', 'Steganography'),
(38, 'C', 'Encryption'),
(38, 'D', 'Data Masking');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(38, 'A');

-- Question 39
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which of the following ports should be disabled or carefully monitored to prevent unauthorized Voice over IP (VoIP) signaling, which can be an avenue for toll fraud or unauthorized call control?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(39, 'A', 'Port 5060'),
(39, 'B', 'Port 161'),
(39, 'C', 'Port 139'),
(39, 'D', 'Port 110');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(39, 'A');

-- Question 40
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'When integrating Cloud services with external applications, which of the following considerations is the most crucial in assessing the security risks associated with data transmission to these external service providers?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(40, 'A', 'Virtualization isolation'),
(40, 'B', 'Encryption during transmission'),
(40, 'C', 'Access control policies'),
(40, 'D', 'Endpoint security');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(40, 'B');

-- Question 41
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Rippled, a drink vendor, is developing a disaster recovery plan to ensure the swift recovery of critical systems and processes in the event of a disruption. They are defining a specific metric which is the amount of acceptable amount of time it will take to return to normal business. What measure are they defining?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(41, 'A', 'RTO'),
(41, 'B', 'MTBF'),
(41, 'C', 'MTTR'),
(41, 'D', 'RPO');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(41, 'A');

-- Question 42
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which of the following is the BEST type of backup that allows for the rapid redeployment of an OS without requiring reinstallation of third-party software, patches, and configurations?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(42, 'A', 'Incremental backup'),
(42, 'B', 'File-level backup'),
(42, 'C', 'Differential backup'),
(42, 'D', 'Image backup');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(42, 'D');

-- Question 43
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Manar is reviewing logs and finds that many logon attempts were made using common words followed by numbers or symbols. Each password is attempted on the 20 computers in the accounting department. He suspects that these passwords were generated by an automated tool. Which of the following password attacks is BEST illustrated by this finding?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(43, 'A', 'Spraying'),
(43, 'B', 'Brute force'),
(43, 'C', 'Downgrade'),
(43, 'D', 'Birthday');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(43, 'A');

-- Question 44
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'At a high-security research facility, employees have been noticing some oddities. Every morning for a week, when the first employee arrives, they find the main entrance door slightly ajar, though nothing inside seems to be stolen or disturbed. The facility uses a high-tech access card system for entry, and logs show different authorized personnel supposedly accessing the building multiple times during the night. However, those employees claim they were at home during those hours. What type of malicious activity is MOST likely responsible for these oddities?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(44, 'A', 'Environmental attack'),
(44, 'B', 'Brute force'),
(44, 'C', 'RFID cloning'),
(44, 'D', 'Malware');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(44, 'C');

-- Question 45
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'You are an IT security manager for an enterprise that deals with sensitive customer information and intellectual property. The organization is concerned about data loss through email and removable storage devices. As a security manager, you recommend implementing a Data Loss Prevention (DLP) solution to enhance security. Which of the following configurations would be the MOST effective way to implement Data Loss Prevention (DLP) for the given scenario?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(45, 'A', 'Configuring the DLP solution to scan all outbound emails and files leaving the organization for sensitive information'),
(45, 'B', 'Using the DLP solution solely for monitoring purposes without implementing any preventive measures'),
(45, 'C', 'Enabling the DLP solution to block all email attachments and USB storage devices to prevent data leakage'),
(45, 'D', 'Implementing DLP on endpoints with a focus on monitoring and preventing data transfers between internal users');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(45, 'A');

-- Question 46
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Dion Training is deploying a new application for remote employees. They want to ensure that users can securely log in without needing a physical device other than their smartphones. The system would generate a temporary numeric code on the user''s device, which would then be used as a second form of authentication. Which of the following solutions BEST fulfills this requirement?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(46, 'A', 'Software authentication tokens'),
(46, 'B', 'Network location-based authentication'),
(46, 'C', 'Static password'),
(46, 'D', 'Biometric authentication');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(46, 'A');

-- Question 47
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Sasha, a network administrator for Kelly''s Technical Innovations, has just recently installed a NGFW on her company’s network to replace the previous traditional stateful firewall they were using. This change was made to keep up with shortcomings that were with the previous firewall. Which of the following improvements does this NGFW provide that were not available previously? (Select all that apply.)', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(47, 'A', 'Can be integrated with various other security products'),
(47, 'B', 'Improved awareness of connection states on layer 4 traffic'),
(47, 'C', 'Application awareness that can distinguish between different types of traffic'),
(47, 'D', 'Addition of multiple functions, including firewall, intrusion prevention, antivirus, and more'),
(47, 'E', 'Ability to conduct deep packet inspection and use signature-based intrusion detection'),
(47, 'F', 'Increased focus on HTTP traffic, helping to prevent common web application attacks like cross-site scripting and SQL injections');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(47, 'A'),
(47, 'C'),
(47, 'E');

-- Question 48
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'A company wants to test a new software application that was downloaded from an unknown source. The company does not want to risk infecting its network or compromising its data with malware or other threats. Which of the following techniques would be the MOST suitable for this scenario?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(48, 'A', 'Sandboxing'),
(48, 'B', 'Firewall'),
(48, 'C', 'Antivirus'),
(48, 'D', 'Encryption');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(48, 'A');

-- Question 49
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which of the following BEST defines the term that represents the expected number of times a risk event will occur within a one-year period?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(49, 'A', 'ARO'),
(49, 'B', 'ALE'),
(49, 'C', 'EF'),
(49, 'D', 'SLE');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(49, 'A');

-- Question 50
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'David is analyzing a recent risk report and categorizes risks based on their likelihood and potential impact, without assigning specific financial values. This approach helps his team prioritize which risks to address first but does not offer detailed monetary estimates. What method is David using?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(50, 'A', 'Residual Risk Analysis'),
(50, 'B', 'Qualitative Risk Assessment'),
(50, 'C', 'Quantitative Risk Assessment'),
(50, 'D', 'Threat Vector Analysis');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(50, 'B');

-- Question 51
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which of the following BEST describes the primary role of an audit committee in the context of cybersecurity?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(51, 'A', 'Handling the execution and implementation of cybersecurity measures.'),
(51, 'B', 'Overseeing cybersecurity risks and ensuring regulatory compliance.'),
(51, 'C', 'Directly managing IT teams to address every security incident in the organization.'),
(51, 'D', 'Engaging in comprehensive policy negotiations with cybersecurity insurance providers.');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(51, 'B');

-- Question 52
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Members of the Risk Management Team at Eclipse, an awning manufacturer, are discussing the organization''s approach to risk management. They are considering the level of risk they are willing to accept to achieve the aggressive set of goals the CEO has created. What is the term for what they are considering?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(52, 'A', 'Risk acceptance'),
(52, 'B', 'Risk tolerance'),
(52, 'C', 'Risk appetite'),
(52, 'D', 'Risk deterrence');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(52, 'C');

-- Question 53
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'A severe storm disrupts power at a company’s main data center, leaving essential systems offline. To maintain operations, the IT team initiates procedures to bring up backup systems at an alternate location and restore critical data. Which aspect of the organization’s disaster recovery policy is being implemented in this scenario?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(53, 'A', 'Risk assessment'),
(53, 'B', 'Recovery and restoration processes'),
(53, 'C', 'Business continuity planning'),
(53, 'D', 'Data redundancy testing');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(53, 'B');

-- Question 54
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Jasmine, the manager of a local bank, was puzzled. Every Monday morning, she would find her safe''s electronic keypad non-responsive, showing a maximum attempts reached error message. However, security footage did not show anyone physically attempting to open the safe over the weekend. Which of the following types of malicious activities is BEST described in this scenario?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(54, 'A', 'Phishing'),
(54, 'B', 'Brute force'),
(54, 'C', 'Environmental attack'),
(54, 'D', 'RFID cloning');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(54, 'B');

-- Question 55
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Jimmy, a Chief Technology Officer, is evaluating different architecture models. His biggest concern is the ease of deployment. Which of the following factors would be MOST critical to consider from a security standpoint?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(55, 'A', 'The vendor''s market reputation'),
(55, 'B', 'Integration with existing security protocols'),
(55, 'C', 'Scalability potential of the architecture'),
(55, 'D', 'Total cost of ownership (TCO)');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(55, 'B');

-- Question 56
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which of the following is NOT true about environmental variables?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(56, 'A', 'Environmental variables, like power supply and cooling, are crucial to ensure the longevity of hardware assets'),
(56, 'B', 'Environmental variables such as temperature and humidity can have significant impacts on hardware performance'),
(56, 'C', 'Knowing the environmental variables helps in managing the needs of different hardware and software in a data center'),
(56, 'D', 'Maintaining standard levels of environmental variables isn''t necessary in most data center environments');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(56, 'D');

-- Question 57
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which of the following BEST describes the primary purpose of e-discovery in digital investigations?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(57, 'A', 'It aids in identifying, collecting, and producing electronically stored information for legal cases'),
(57, 'B', 'It sets guidelines for selecting appropriate forensic software tools throughout the investigation'),
(57, 'C', 'It offers insights into the potential financial consequences of an incident being investigated'),
(57, 'D', 'It provides methodologies to ensure consistent data protection during the investigation process');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(57, 'A');

-- Question 58
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which of the following hardware vulnerability involves the ability to modify the software that controls the functionality of a device?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(58, 'A', 'Side loading'),
(58, 'B', 'Legacy vulnerability'),
(58, 'C', 'End-of-life vulnerability'),
(58, 'D', 'Firmware vulnerability');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(58, 'D');

-- Question 59
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'At DionTraining, the risk management team has completed a comprehensive risk assessment and identified potential risks across various departments. To ensure proactive risk management and response, they want to establish a system for continuously monitoring and tracking these identified risks. Which element of the risk management process should the risk management team implement to monitor and track the identified risks over time?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(59, 'A', 'Risk assessment'),
(59, 'B', 'Risk register'),
(59, 'C', 'Risk reporting'),
(59, 'D', 'Business impact analysis');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(59, 'B');

-- Question 60
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'A security officer at Kelly Innovations LLC is reviewing recent security incidents to assess potential threats within the organization. Two patterns of behavior have raised concerns about a possible insider threat. Which of the following are signs of potential insider threat? (Select TWO.)', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(60, 'A', 'Policy advocacy'),
(60, 'B', 'Frequent unauthorized access'),
(60, 'C', 'Increased work hours'),
(60, 'D', 'Unusual data transfers'),
(60, 'E', 'Irregular system maintenance');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(60, 'B'),
(60, 'D');

-- Question 61
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which of the following techniques allows an attacker to eavesdrop on a wired network by connecting their device directly to the network cables?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(61, 'A', 'Packet Sniffing'),
(61, 'B', 'Port Mirroring'),
(61, 'C', 'On-path attack'),
(61, 'D', 'Wiretapping');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(61, 'D');

-- Question 62
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which of the following statements is NOT true about the importance of continuous integration in relation to secure operations?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(62, 'A', 'Continuous integration may slow down the development process but it provides far more secure systems overall'),
(62, 'B', 'Continuous integration can increase software quality by catching and fixing bugs quickly'),
(62, 'C', 'Continuous integration automates the building and testing of code, which enhances developer productivity'),
(62, 'D', 'Continuous integration enables early detection of issues, making it easier to address them before they escalate');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(62, 'A');

-- Question 63
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which term refers to the percentage of an asset''s value that is expected to be lost when a specific risk eventuates?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(63, 'A', 'Damage proportion'),
(63, 'B', 'EF'),
(63, 'C', 'SLE'),
(63, 'D', 'Asset impact');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(63, 'B');

-- Question 64
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Lexicon, an AI company, seeks to implement a security measure to systematically identify, evaluate, and prioritize potential risks to their systems and networks. Which of the following is an example of a managerial security control that would help achieve this?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(64, 'A', 'Security Guards'),
(64, 'B', 'Risk assessments'),
(64, 'C', 'Intrusion detection system'),
(64, 'D', 'Firewall');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(64, 'B');

-- Question 65
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Jamario, an IT administrator for Dion Training Solutions, is considering deploying an agent-based web filter solution to manage and monitor web traffic for remote employees. Which of the following is the MOST important advantage of implementing agent-based web filters over traditional gateway-based filters for this purpose?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(65, 'A', 'It doesn’t require any updates or maintenance'),
(65, 'B', 'It allows for consistent policy enforcement regardless of the user''s location'),
(65, 'C', 'It reduces the total cost of ownership (TCO) due to the absence of hardware'),
(65, 'D', 'It can filter traffic at a faster rate than gateway solutions');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(65, 'B');

-- Question 66
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which of the following is a disadvantage of agentless posture assessment in Network Access Control (NAC) solutions?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(66, 'A', 'Less detailed information about the client is available'),
(66, 'B', 'Requires more storage space on the client device'),
(66, 'C', 'Inability to support smartphones, tablets, and IoT devices'),
(66, 'D', 'Increased risk of malware infection on client devices');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(66, 'A');

-- Question 67
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which of the following BEST describes the role of classification in effective hardware, software, and data asset management?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(67, 'A', 'Classification helps in tracking the financial value of assets'),
(67, 'B', 'Classification allows organizations can track their physical location across multiple locations'),
(67, 'C', 'Classification establishes accountability for asset usage'),
(67, 'D', 'Classification ensures that assets are labeled with appropriate access levels');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(67, 'D');

-- Question 68
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'What part of a BPA for mission essential functions provides a detailed, step-by-step description of the procedural tasks performed?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(68, 'A', 'Hardware'),
(68, 'B', 'Process flow'),
(68, 'C', 'Inputs'),
(68, 'D', 'Outputs');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(68, 'B');

-- Question 69
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'In the realm of digital forensics, which activity is a primary focus during the preservation phase?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(69, 'A', 'Performing keyword searches on electronic documents to identify pertinent information'),
(69, 'B', 'Drafting a comprehensive summary of findings and presenting it to stakeholders'),
(69, 'C', 'Generating and documenting cryptographic hashes of digital evidence to verify its integrity'),
(69, 'D', 'Recording the specific tools and methodologies used during the evidence collection phase');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(69, 'C');

-- Question 70
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'As a network administrator responsible for evaluating a company''s encryption protocol method for wireless devices, you have discovered that the company is currently utilizing a deprecated encryption protocol that poses a significant security threat. Which of the following is the MOST appropriate encryption protocol to recommend upgrading to?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(70, 'A', 'WPA'),
(70, 'B', 'TKIP'),
(70, 'C', 'WEP'),
(70, 'D', 'AES');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(70, 'D');

-- Question 71
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which of the following statements is NOT true concerning the significance of NetFlow?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(71, 'A', 'NetFlow can help with capacity planning and understanding network performance issues'),
(71, 'B', 'NetFlow can interpret traffic flow patterns and identify the type of network attack that is occurring'),
(71, 'C', 'NetFlow can identify the source and destination of traffic, making it easier to spot potential threats'),
(71, 'D', 'NetFlow helps provide an understanding of network traffic flow, enhancing security by identifying unusual patterns');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(71, 'B');

-- Question 72
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'As a security analyst, you are reviewing application logs while investigating a suspected breach. Which of the following pieces of information is NOT typically documented in the application log data?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(72, 'A', 'Server IP address where the application is hosted'),
(72, 'B', 'Timestamps of application activity'),
(72, 'C', 'The physical location of the user accessing the application'),
(72, 'D', 'User IDs related to specific application transactions');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(72, 'C');

-- Question 73
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which of the following solutions should a data center implement to guarantee customer data remains unreadable in the event of a physical server compromise?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(73, 'A', 'Server clustering'),
(73, 'B', 'Data deduplication'),
(73, 'C', 'RAID'),
(73, 'D', 'Full disk encryption');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(73, 'D');

-- Question 74
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'The New York Inquirer''s main headquarters has a diverse IT infrastructure, including servers, workstations, and IoT devices. They have implemented a firewall to protect their internal network from external threats. The organization wants to modify the firewall rules to enhance security and minimize potential attack vectors. Which modification to firewall ports and protocols is NOT recommended for the organization to enhance security?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(74, 'A', 'Enabling stateful Inspection for packet filtering'),
(74, 'B', 'Closing unused and unnecessary ports and protocols'),
(74, 'C', 'Allowing any outgoing traffic to any destination'),
(74, 'D', 'Implementing port forwarding for remote access to internal servers');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(74, 'C');

-- Question 75
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'An organization hires a third-party vendor to handle its data storage needs. To ensure data confidentiality and establish clear expectations around responsibilities, they sign a document that outlines security controls, availability requirements, and confidentiality clauses. Which type of agreement is this document?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(75, 'A', 'Memorandum of Understanding (MOU)'),
(75, 'B', 'Data Use Agreement (DUA)'),
(75, 'C', 'Service Level Agreement (SLA)'),
(75, 'D', 'Business Partnership Agreement (BPA)');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(75, 'C');

-- Question 76
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Morris has organized an exercise for his security team to test their new defense plans. He has divided the team into two groups: one defending the system and the other attempting to breach it. The groups, set up with similar experience and size, will compete, and the winning team will have lunch catered. What type of exercise has Morris created?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(76, 'A', 'Functional exercise'),
(76, 'B', 'Tabletop exercise'),
(76, 'C', 'Simulation'),
(76, 'D', 'Failover');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(76, 'C');

-- Question 77
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which of the following approaches ensures real-time or near-real-time duplication of data to a secondary location for purposes like high availability, disaster recovery, and load balancing?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(77, 'A', 'Snapshots'),
(77, 'B', 'Journaling'),
(77, 'C', 'Differential backups'),
(77, 'D', 'Replication');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(77, 'D');

-- Question 78
INSERT INTO questions (subject_id, question_text, question_type) VALUES
(1, 'Which technique, when considering high availability, involves distributing network or application traffic across a number of servers to enhance the performance and reliability of applications?', 'multiple_choice');

INSERT INTO options (question_id, option_key, option_text) VALUES
(78, 'A', 'Clustering'),
(78, 'B', 'Load balancing'),
(78, 'C', 'Frequency'),
(78, 'D', 'Geographic dispersion');

INSERT INTO correct_answers (question_id, answer_key) VALUES
(78, 'B');
