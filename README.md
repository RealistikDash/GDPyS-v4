<img width="128" align="left" style="float: left; margin: 0 10px 0 0;" alt="GDPyS" src="https://cdn.discordapp.com/icons/726830621556736141/29d38660477666e5eabb790febe7dc0c.webp">

# GDPyS-v4
An implementation of the Geometry Dash server written in asynchronous Python meant for production.
Designed with the intention of allowing individuals to create their own instances of Geometry Dash Private Servers (GDPS).

## Requirements
- Server running Linux

The specifications of the server fully depend on the scale of the server (with lower size servers having very low requirements). Recommended distributions include Ubuntu Server.

- Python >3.9

With GDPyS being a modern server implementation, it relies on some of the newest features of the Python programming language.

- MySQL/MariaDB Database

A MySQL database is utilised by GDPyS for the bulk of the data storage. It is a tried, tested, fast and reliable form of mass data storage.

- Redis Database

Redis allows GDPyS to easily manage its cached values, share data between applications and allow 3rd party applications to easily integrate with GDPyS' inner workings.

- MeiliSearch

Meilisearch is a powerful search engine utilised by GDPyS for level and user searches. It offers great features such as typo detection, allowing for fast and accurate search results.

### Recommendations
These are not required for GDPyS to run, however are highly recommended for production settings.

- Nginx

Nginx is a powerful web server allowing for powerful config building alongside adding another layer of protection.

- Cloudflare

Cloudflare is a popular tool utilised by most websites as another layer of protection for any potential abuse. Alongside this, it offers all web application features such as geolocation, which GDPyS is able to benefit from.

- Datadog

Datadog is a highly useful statistics tool used to see how well your server is running with the current demand. GDPyS offers a built in integration with the free service.

- Uvicorn

Uvicorn is a server runner that integrates extremely well with GDPyS' framework of choice, Starlette. Its workers feature allows GDPyS to take advantage of multiple CPU threads, increasing performance.
