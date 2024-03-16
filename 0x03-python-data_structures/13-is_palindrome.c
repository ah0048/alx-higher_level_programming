#include "lists.h"
/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: pointer to list to be checked
 * Return: 0 if palindrome or 1 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *first, *second;

	slow = *head;
	fast = *head;
	first = *head;
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	if (fast)
	{
		slow = slow->next;
	}
	second = slow;
	reverse_list(&second);
	while (second)
	{
		if (second->n != first->n)
			return (0);
		first = first->next;
		second = second->next;
	}
	return (1);
}
/**
 * reverse_list - reverse a linked list
 * @head: pointer to list to be checked
 * Return: void
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current, *next;

	current = *head;
	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
