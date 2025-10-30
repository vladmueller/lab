package de.vladmueller.opencqrs;

import com.opencqrs.framework.command.Command;
import java.util.UUID;

public record PurchaseBookCommand(
    UUID id,
    String isbn,
    String title,
    String author,
    Long numPages
) implements Command {

    @Override
    public String getSubject() {
        return "/books/" + id();
    }
}
