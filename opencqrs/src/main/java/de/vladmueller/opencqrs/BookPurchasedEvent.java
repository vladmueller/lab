package de.vladmueller.opencqrs;

import java.util.UUID;

public record BookPurchasedEvent(
    UUID id,
    String isbn,
    String title,
    String author,
    Long numPages
) {}
