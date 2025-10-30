package de.vladmueller.opencqrs;

import com.opencqrs.framework.command.CommandEventPublisher;
import com.opencqrs.framework.command.CommandHandlerConfiguration;
import com.opencqrs.framework.command.CommandHandling;

@CommandHandlerConfiguration
public class BookHandling {

    @CommandHandling
    public void handle(PurchaseBookCommand command, CommandEventPublisher<Void> publisher) {
        publisher.publish(
            new BookPurchasedEvent(
                command.id(),
                command.isbn(),
                command.title(),
                command.author(),
                command.numPages()
            )
        );
    }
}
