package main

from summarizer import Summarizer

import (
        "fmt"
        "log"
        "net/http"
        "os"
)

func handler(w http.ResponseWriter, r *http.Request) {
        log.Print("helloworld: received a request")
        target := os.Getenv("TARGET")
        if target == "" {
                target = "World"
        }
        fmt.Fprintf(w, "Hello %s!\n", target)
}

func main() {
        log.Print("helloworld: starting server...")

        http.HandleFunc("/", handler)

        port := os.Getenv("PORT")
        if port == "" {
        	port = "0.0.0.0"
        }

		body = 'Text body that you want to summarize with BERT'
		model = Summarizer()
		print(model(body))

        log.Printf("helloworld: listening on port %s", port)
        log.Fatal(http.ListenAndServe(fmt.Sprintf(":%s", port), nil))
}


