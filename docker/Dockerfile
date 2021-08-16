FROM golang:1.10 AS builder              
# Создаем временный Докер-образ и называем его builder                    
WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

FROM alpine:latest                       
# Создаем финальный Докер-образ на базе легковесного alpine
RUN apk --no-cache add ca-certificates  
WORKDIR /root/
COPY --from=builder ./app .              
# Копируем собранное приложение из образа biulder
EXPOSE 8080
CMD ["./app"]