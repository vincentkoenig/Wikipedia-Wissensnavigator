import wikipedia

WIKI_INPUT = "Olympische Spiele"
wikipedia.set_lang("de")
wikipedia.set_user_agent("Wikipedia-Wissensnavigator/1.0 (https://github.com/vincentkoenig/Wikipedia-Wissensnavigator)")

def is_wiki_content_found(topic):
    """
    Prüft, ob zu einem gegebenen Wikipedia-Thema eine gültige Seite
    existiert.
    Die Funktion versucht die entsprechende Wikipedia-Seite zu laden.
    Bei Erfolg wird das vollständige Wiki-Objekt zurückgegeben.
    Bei Mehrdeutigkeiten (DisambiguationError) werden bis zu 5 alternative
    Seitentitel zurückgegeben.
    Bei nicht existierenden Seiten (PageError) werden bis zu 5 Suchvorschläge
    zurückgegeben.
    :param topic: str
        Der Titel oder Suchbegriff des Wiki-Artikels.
    :return:
        tupel: (Wiki-Objekt, None) bei Erfolg,
                (None, Liste[strings]) bei Mehrdeutigkeit oder fehlender Seite
    """
    try:
        wiki_full = wikipedia.page(topic, auto_suggest=False)
        return wiki_full, None
    except wikipedia.DisambiguationError as e:
        return None, e.options[:5]
    except wikipedia.PageError as e:
        wiki_search = wikipedia.search(topic, results=5)
        return None, wiki_search


def get_wiki_content(topic):
    """
    Ruft den vollständigen Textinhalt eines Wikipedia-Artikels ab.
    Die Funktion nutzt "is_wiki_content_found()" um zu prüfen, ob eine
    gültige Seite existiert. Falls ja, wird der gesamte Artikelinhalt
    zurückgegeben. Falls nicht, werden alternative Vorschläge oder
    Suchergebnisse zurückgegeben, die dem Nutzer helfen können, den richtigen
    Artikel zu finden.
    :param topic: str
        Der Titel oder Suchbegriff des Wiki-Artikels.
    :return:
        tuple:
            (content, None) bei Erfolg,
            (None, Liste[strings]) bei Mehrdeutigkeit oder fehlender Seite
    """
    wiki_full, wiki_search = is_wiki_content_found(topic)
    if wiki_full:
        return wiki_full.content, None
    else:
        return None, wiki_search


def get_wiki_url(topic):
    """
    Ruft die URL eines Wikipedia-Artikels ab.
    Die Funktion nutzt "is_wiki_content_found()" um zu prüfen, ob eine
    gültige Seite existiert. Falls ja, wird die URL des Artikels
    zurückgegeben. Falls nicht, werden alternative Vorschläge oder
    Suchergebnisse zurückgegeben, die dem Nutzer helfen können, den richtigen
    Artikel zu finden.
    :param topic: str
        Der Titel oder Suchbegriff des Wiki-Artikels.
    :return:
        tuple:
            (url, None) bei Erfolg,
            (None, Liste[strings]) bei Mehrdeutigkeit oder fehlender Seite
    """
    wiki_full, wiki_search = is_wiki_content_found(topic)
    if wiki_full:
        return wiki_full.url, None
    else:
        return None, wiki_search

