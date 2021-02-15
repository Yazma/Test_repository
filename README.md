
##Per lanciare l'applicazione:

	Per poter utilizzare la classe emailProcess è sufficente avere installato python 3.6


##Descrizione dell'applicazione:

	La classe emailProcess permette di inviare email programmaticamente tramite il metodo send_mail.
	Possono essere inviati file allegati, sono stati testati i tipi di file quali: word, excel, csv, txt, pdf, powerpoint.
	In base al numero di allegati e alla loro grandezza il processo può impiegare più tempo.
	Devono essere rispettate le seguenti regole per l'utilizzo di questa classe.
	Il parametro "body type" può attualmente essere impostato come "plain" se il corpo della mail sarà di tipo testo, altrimenti come "html" se il corpo della mail sarà un html.
	Il parametro "server" indica a quale server di posta ci si sta collegando, attaulmente si possono utilizzare quelli di outlook, "smtp-mail.outlook.com", o quelli gmail, "smtp.gmail.com".
	Per allegare dei file è necessario specificare l'intero path del file + nome del file e la sua estensione nella lista list_of_path_name_attachment; deve essere inoltre inserito il nome del file e la sua estenzione nella posizione corrispondente nella lista "list_of_file_name_attachment".
	Alla fine dello script è presente un esempio di utilizzo.
