The Python script that add and remove entries and create HTML files from the MySQL database require Pip to be used to install mysql.connector. The script does not work otherwise.

# KCHS
Photo Database Proposal for the Knox County Historical Society

1. Introduction

  The Knox County Historical Society (KCHS) aims to improve the organization, access, and preservation of its extensive collection of photographs and negatives. Currently, the society lacks an efficient method for storing and retrieving images based on key identifying information. This proposal outlines the development of a software system to meet these needs by allowing photographs and negatives to be entered, stored, and searched through a robust and user-friendly database system.

2. Problem Statement

  The KCHS currently faces the challenge of efficiently organizing and searching their vast collection of photographs and negatives. With no digital database, the task of managing and accessing specific photos is cumbersome and time-consuming. There is a need for a comprehensive database system that allows photographs to be scanned, categorized, and searched by various fields, such as date, title, and description. This system will facilitate easier access to historical photos for the public and streamline the workflow for KCHS personnel.

3. Proposed Solution

  We propose developing a software system that will allow the KCHS to scan, organize, store, and search their collection of photographs and negatives. The system will consist of a secure, scalable database and an easy-to-use front-end interface to support both administrative and public access. The database will include multiple fields for sorting and searching photos, enabling users to find specific images based on various criteria.
Key Features:
  - Photograph and Negative Entry: The system will support the entry of scanned photographs and negatives, with fields for metadata including type, date, title,     - description, dimensions, people’s names, and more.
  - Search Functionality: Users can search the database by multiple fields (e.g., date, title, people’s names, photo type).
  - Image Storage: Photographs and negatives will be securely stored and accessible via the database, ensuring proper digital preservation.
  - Public Access: Selected images will be made publicly accessible through a web interface, allowing users to explore historical photographs relevant to Knox         County.
  - Administrative Tools: KCHS personnel will be able to add, update, and remove records as needed. They will also have access to advanced sorting and reporting       functions for easier inventory management.

4. Stakeholders

  The success of this project depends on the collaboration and needs of the following stakeholders:
  - KCHS Personnel: These users will input, update, and manage photographs and negatives. They will rely on the system to keep the collection organized and            accessible.
  - Researchers & General Public: Individuals who wish to explore historical photographs of Knox County, Ohio, will access the public interface to search for          specific images.

5. Project Goals

  The primary goal of this project is to create a fully functioning photo database system for the KCHS. The system will provide the following key benefits:
Improved organization of the photo collection, with easy entry of new photographs and negatives.
Advanced searchability based on multiple metadata fields.
Secure storage of the images and their associated metadata.
Public access to selected historical images, contributing to the preservation and sharing of Knox County history.

6. Major Functions and Attributes

6.1 Photograph and Negative Entry
  - Ability to scan and upload photos and negatives.
  - Fields for metadata entry: Box labels, date, title, photo type, description, dimensions, people’s names, occupation, etc.
6.2 Search and Sort Functionality
  - Users can search by multiple fields: Date, Title, People’s Names, Occupation, etc.
  - Filters to allow sorting by metadata fields, such as category, type, or year.
6.3 Public Access
  - Web-based interface for the general public to view and search photos.
6.4 Administrative Interface
  - KCHS staff will have a secure login to access administrative features, such as adding, removing, and editing metadata records.
6.5 Image Storage
  - Photos will be stored in a secure, organized directory system.
6.6 PastPerfect Integration
  - Allow for the possibility of integrating database into the PastPerfect Model

7. Data Management

  The database system will consist of two primary components:
Photo Files: These will be stored in a secure digital format and organized by metadata fields for easy retrieval.
Metadata: Each photograph will have corresponding metadata, stored in a structured relational database for efficient querying.
The system will allow the KCHS to manage, update, and back up both the photographs and their associated metadata. There will be regular data backups to ensure the longevity of the collection.

8. Technical Requirements

  Database Management System: Relational database (e.g., MySQL, PostgreSQL) for storing photo metadata.
Web Interface: A front-end web application built using a modern framework (e.g., HTML) for public access.
Backend Development: A backend system to manage database interactions, authentication, and image storage.
Image Storage: A secure cloud-based or local server solution to store photographs and scanned negatives, ensuring both scalability and security.

9. Conclusion

The proposed software system will greatly enhance the ability of the Knox County Historical Society to organize, store, and retrieve historical photographs and negatives. By offering a comprehensive database that is both secure and accessible, this system will not only improve internal workflows but also enable the public to engage with and explore Knox County’s rich history. Through careful planning, development, and collaboration with the KCHS, this project will be a valuable asset for both current and future generations interested in the history of the region.

MEETING NOTES:
- Sort by last name, occupation, etc
- 35mm negative
    - Ex. “4/20/02  — Carnival”
    - Collections of photos
    - We have the newspapers too
- Fields:
    - Primary:
        -ID
        -Date Taken
        -Title
        -Description
        -Link
    -   -Date Added
    - Secondary:
        -Box labels (type photos, category, year)

  The SQL script is run through MySQL workbench, but will be integrated in later versions.
        - Description
        - People’s names, occupations
        - Photo type
        - Dimensions
- PastPerfect integration
