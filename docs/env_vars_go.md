# Env Vars in go

## Env Module

https://github.com/caarlos0/env

```
export MINIO_URL="0.0.0.0:9000"
export MINIO_ACCESS_KEY="ACCESS"
export MINIO_SECRET_KEY="0123456789"
export MINIO_SECURE="false"
export MINIO_BUCKET=$(uuidgen)
```

main.go

```
package main

import (
    "fmt"
    "github.com/caarlos0/env"
    "os"
    "strings"
)

type MinioCfg struct {
    Url       string `env:"MINIO_URL" envDefault:"0.0.0.0:9000"`
    AccessKey string `env:"MINIO_ACCESS_KEY"`
    SecretKey string `env:"MINIO_SECRET_KEY"`
    Secure    bool   `env:"MINIO_SECURE"`
    Bucket    string `env:"MINIO_BUCKET"`
}

func main() {

    cfg := MinioCfg{}
    err := env.Parse(&cfg)

    if err != nil {
        fmt.Printf("%+v\n", err)
    }

    fmt.Printf("%+v\n", cfg)

    for _, e := range os.Environ() {
        pair := strings.Split(e, "=")
        if strings.HasPrefix(pair[0], "MINIO") {
            fmt.Println(pair[0], "=", pair[1])
        }
    }
}
```

## Native

```
package main

import (
    "os"
    "fmt"
)

// GetEnv returns an env variable value or a default
func GetEnv(key, fallback string) string {
    if value, ok := os.LookupEnv(key); ok {
        return value
    }
    return fallback
}

func main() {
    foo := GetEnv("FOO_FOO", "foo_not_set")
    fmt.Printf("foo : %s\n", foo)
}
```


