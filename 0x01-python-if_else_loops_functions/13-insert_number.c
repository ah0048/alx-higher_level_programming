#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - insert a node in a linked list
 * @head: pointer to node
 * @number: number to be stored
 * Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new = malloc(sizeof(listint_t));

    listint_t *node = *head;

    if (new == NULL)
        return (NULL);
    new->n = number;
    new->next = NULL;
    if (node == NULL || new->n <= node->n)
        {
            new->next = node;
            return (*head = new);
        }
    while (node)
    {
        if (node->next == NULL || new->n < node->next->n)
        {
            new->next = node->next;
            node->next = new;
            return (node);
        }
        node = node->next;
    }
    return (NULL);
}
