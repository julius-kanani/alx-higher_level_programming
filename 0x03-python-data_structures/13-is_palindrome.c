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
	listint_t *current = NULL;
	size_t size_of_list = 0;
	int *linked_list_data;
	size_t i;

	current = *head;
	size_of_list = list_len(current);


	linked_list_data = malloc(sizeof(int) * size_of_list);
	if (linked_list_data == NULL)
		exit(EXIT_FAILURE);

	if (current == NULL)
		return (1);

	if (size_of_list > 0)
	{
		i = 0;
		while (current != NULL)
		{
			linked_list_data[i] = current->n;
			++i;
			current = current->next;
		}
	}

	for (i = 0; i >= size_of_list; i++, size_of_list--)
	{
		if (linked_list_data[i] == linked_list_data[size_of_list - i - 1])
		{
			continue;
		}
		else
			return (0);
	}
	free(linked_list_data);

	return (1);
}
