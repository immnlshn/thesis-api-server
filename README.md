# thesis-api-server

Dieses Projekt ist das Backend für die Bachelorarbeit:

**„Migration bestehender Webkomponenten zu einer zustands- und komponentenbasierten Frontend-Architektur“**

Kapitel 3.3.1 – Beispielhafte Implementierung eines Quiz-Backends

---

## Übersicht

Dieses Backend stellt eine REST-API für ein Quiz-System bereit. Es dient als Beispiel für die Anbindung moderner Frontend-Architekturen.
Es ermöglicht die Durchführung von Quizfragen, das Speichern von Antworten und die Auswertung der Ergebnisse. Die API ist mit FastAPI implementiert und nutzt Pydantic für die Datenvalidierung.

**Zugehörige Frontends:**
- [thesis-react-redux (React + Redux Toolkit + TypeScript)](https://github.com/immnlshn/thesis-react-redux)
- [thesis-react-xstate (React + XState + TypeScript)](https://github.com/immnlshn/thesis-react-xstate)

---

## Features

- Bereitstellung von Quizfragen als JSON
- Verwaltung von Quiz-Sessions (Start, Antworten, Ergebnis)
- REST-API mit FastAPI
- Datenhaltung über JSON-Datei (keine Datenbank nötig)
- Einfache Erweiterbarkeit und Anpassbarkeit

---

## Projektstruktur

- **main.py** – Einstiegspunkt, FastAPI-Server und Endpunkte
- **data/questions.json** – Fragenpool (kann angepasst/erweitert werden)
- **models/** – Pydantic-Modelle für Datenvalidierung (Question, Answer, QuizSession, ...)

---

## Entwicklung & Start

1. **Abhängigkeiten installieren:**
   
   Stelle sicher, dass Python 3.10+ installiert ist.
   
   ```bash
   pip install fastapi uvicorn
   ```

2. **Server starten:**
   
   ```bash
   uvicorn main:app --reload
   ```

3. **API-Dokumentation:**
   
   Nach dem Start ist die interaktive API unter [http://localhost:8000/docs](http://localhost:8000/docs) erreichbar.

---

## Endpunkte (Beispiel)

- `POST /quiz/start` – Startet eine neue Quiz-Session
- `POST /quiz/answer` – Antwortet auf eine Frage
- `GET /quiz/result/{session_id}` – Holt das Ergebnis einer Session

Die genaue API-Struktur ist in `main.py` dokumentiert und über Swagger UI einsehbar.

---

## Hinweise

- Das Backend ist für Demonstrations- und Analysezwecke im Rahmen der Bachelorarbeit konzipiert.
- Es werden keine Benutzerdaten gespeichert, Sessions sind temporär.
- Die Fragen können in `data/questions.json` angepasst werden.
