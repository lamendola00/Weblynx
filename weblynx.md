# Descrizione del Progetto di Applicazione Web

## Introduzione
Mi è stato assegnato un altro progetto di applicazione web. 
Lo scopo principale del progetto è creare un'applicazione web senza login 
che possa raccogliere e mostrare link inseriti dagli utenti che vi accedono. 
Ciò permetterà di raccogliere tutti i link in un'unica applicazione accessibile 
da qualsiasi browser, risolvendo così il problema dei segnalibri 
dispersi tra vari browser.

### Legenda:
- (ob) Campo Obbligatorio
- (fa) Campo Facoltativo

## View:

### (1) Pagina Principale:
- Mostra i link presenti nel database in formato tabella, 
ogni link visualizzato singolarmente in ogni riga, 
con immagine, descrizione, tag degli utenti (opzionale)
 e la possibilità di cliccare sul link per visitarlo e modificarlo (3).
- Fornisce opzioni di filtraggio in alto a destra 
per filtrare per categoria e utenti taggati, 
così come opzioni di ordinamento per data di aggiunta.
- Include tre pulsanti in alto a sinistra per aggiungere, 
aggiornare e cancellare link.

### (2) Pagina Dettaglio Link:
- Mostra il link selezionato all'interno di una forma quadrata/rettangolare 
come se fosse una scheda prodotto:
  - Titolo in alto
  - Immagine e descrizione più grandi, eventualmente con sottolink (da valutare)
  - Tag in una colonna a destra o sinistra della figura geometrica 
  che mostra le specifiche del link
  - Due pulsanti in alto a sinistra per modificare ed eliminare il link

### (3) Pagina Modifica Link:
- Consente la modifica dei dettagli del link, 
con gli stessi campi della pagina (4) ma pre-compilati ed editabili. 
Fornisce opzioni per salvare o cancellare in alto a sinistra.

### (4) Pagina Form Inserimento Link:
- Contiene campi per l'inserimento di un nuovo link:
  - Titolo
  - Link
  - Immagine opzionale
  - Descrizione
  - Tag di uno o più utenti
- Include pulsanti per salvare il link (salva e ritorna alla pagina 1)
o cancellare il link (cancella tutti i campi e ritorna alla pagina 1)

### Pagine Opzionali:
- **(5) Pagina Gestione Errori:** Gestisce errori come link non funzionanti o 
altri errori
- **(6) Pagina Statistiche:** Mostra statistiche sui link più cliccati o 
altri dati rilevanti

## Implementazione del Progetto:
L'idea è partire con un'applicazione basica e funzionale, successivamente 
aggiungere funzionalità come filtraggio/ordinamento o miglioramenti dell'UI. 
L'obiettivo principale è accedere ai dati del database e visualizzarli, 
garantendo la possibilità di mostrare righe aggiornate all'ultima modifica,
modificarle ed eliminarle.

Nella pagina (1), l'interfaccia HTML mostrerà tutti i link presenti 
nel database in formato tabella con righe e colonne multiple, 
che possono essere filtrati e ordinati (successivamente). 
Devono essere visibili una volta inseriti. 
L'inserimento avviene tramite un form che consente di includere un'immagine 
e una descrizione per ogni link. Va valutata la gestione di un grande numero di link;
pertanto, potrebbe essere sensato mostrare tutti i link sulla homepage 
o creare pulsanti molto grandi che filtrano automaticamente i risultati 
e mostrano i link appartenenti a una categoria su un'altra pagina.

Ogni riga del database conterrà:
**t_links:**
- ID del link (PK)
- Link
- Gestione dell'immagine da determinare, localmente o nell'ambiente 
di esecuzione dell'applicazione
- Descrizione (molti caratteri)
- Tag degli utenti (FK)
- Categorie di link (FK)

**t_categories:**
- ID categoria (PK)
- Categorie di link

**t_tag:**
- ID tag (PK)
- Nome del tag


**ENGLISH VERSION**

# Web Application Project Description

## Introduction
The main purpose of the project is to create a web application without login 
that can collect and display links entered by users who access it. 
This will help gather all the links in one application accessible from any browser, 
thereby solving the problem of having bookmarks scattered across various browsers.

### Legend:
- (MF) Mandatory Field
- (OF) Optional Field

## Views:

### (1) Main Page:
- Displays links that are in the database in a table format, 
each link shown individually in each row, with title, attached image, description,
user tags (optional), and the option to click on the link to visit it 
and to modify it (3).
- Provides filtering options at the top right corner to filter by category 
and tagged users, as well as sorting options by addition date.
- Features three buttons at the top left corner to add, update, and delete links.

### (2) Link Detail Page:
- Displays the selected link within a square/rectangular shape as if it were 
a product card:
  - Title at the top
  - Larger image and description, possibly with sublinks (to be evaluated)
  - Tags in a column on the right or left side of the geometric figure 
  displaying link specifications
  - Two buttons at the top left for editing and deleting the link card

### (3) Link Update/delete Page:
- Allows update of the link details, with the same fields as page (4) 
but it will be pre-filled and editable. With save or delete button at the top left.

### (4) Link Insertion Form Page:
- Contains fields for inserting a new link:
  - Title(MF)
  - Link(MF)
  - Image(OF)
  - Description(OF)
  - Tagging of one or more users(OF)
- Includes buttons to save the link (saves and returns to page 1) 
or delete the link (clears all fields and returns to page 1)

### Optional Pages:
- **(5) Error Management Page:** Handles errors such as non-working links 
or other errors
- **(6) Statistics Page:** Displays statistics on the most clicked links 
or other relevant data

## Project Implementation:
The idea is to start with a basic, functional application and after that 
i will add features like filtering/sorting or improving the UI. 
The first goal is to access database data and display it, ensuring the ability 
to show rows updated to the latest modification, as well as modify and delete them.

In page (1), the HTML interface will display all links present 
in the database in a table format with multiple rows and columns, 
which can be filtered and sorted (later). They should be visible once inserted.
Insertion occurs through a form that allows including an image and a description 
for each link. Consideration should be given to managing a large number of links; 
therefore, it may be sensible to either display all links on the homepage or 
create very large buttons that automatically filter results and show links 
belonging to a category on another page.

Each row of the database will contain:
**t_links:**
- Link ID (PK)
- Link
- Image management to be determined, possibly locally or in the application's 
runtime environment
- Description (many characters)
- User tags (FK)
- Link categories (FK)

**t_categories:**
- Category ID (PK)
- Link Categories

**t_tag:**
- Tag ID (PK)
- Tag Name

