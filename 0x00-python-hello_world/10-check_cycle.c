#include "lists.h"
/**
 * check_cycle - checks if the linked list has a cycle
 * @list: pointer to a linked list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;

	listint_t *fast = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
