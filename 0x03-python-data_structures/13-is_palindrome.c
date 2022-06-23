#include "lists.h"

/**
  *list_len - give the number of elements in a list.
  *@h: pointer to list.
  *
  *Return: number of elements in a linked list.
  */
size_t list_len(const listint_t *h)
{
	int count;

	count = 0;
	while (h != NULL)
	{
		count++;
		h = h->next;
	}

	return (count);
}

/**
 * is_palindrome - checks if a singly linked list is palindrome.
 * @head: The start of a singly linked list.
 * Return: 0, if not palindrome, 1, if palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = NULL, *tail = NULL, *cursor = NULL;
	size_t list_size = 0, i;

	current = *head;
	list_size = list_len(current);
	tail = get_last_node(head);
	if (current == NULL)
		return (1);
	if (list_size > 1)
	{
		i = 0;
		while ((i < list_size) && (current != NULL))
		{
			if (current->n == tail->n)
			{
				if ((current == tail) && (current->n == tail->n))
					return (1);
				else if ((current->next == tail) && (current->n == tail->n))
					return (1);
				cursor = current;
				while (cursor != NULL)
				{
					if (cursor->next == tail)
					{
						tail = cursor;
						break;
					}
					cursor = cursor->next;
				}
			}
			else
				return (0);
			--list_size;
			++i;
			current = current->next;
		}
	}
	return (1);

}

/**
 * get_last_node - gets the tail of a singly linked list.
 * @head: The head of a singly linked list.
 * Return: The address of the last node or tail of a list.
 */
listint_t *get_last_node(listint_t **head)
{
	listint_t *tail = NULL, *current = NULL;

	current = *head;

	while (current != NULL)
	{
		if (current->next == NULL)
			tail = current;
		current = current->next;
	}

	return (tail);
}
