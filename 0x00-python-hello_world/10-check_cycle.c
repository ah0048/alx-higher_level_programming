#include "lists.h"
/**
 * check_cycle - checks if the linked list has a cycle
 * @list: pointer to a linked list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;

	listint_t *fast = list->next;

	if (list == NULL || list->next == NULL)
		return (0);
	while (slow != fast)
	{
		if (fast == NULL || fast->next == NULL)
			return (0);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (1);
}
