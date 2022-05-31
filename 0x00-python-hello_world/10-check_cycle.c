#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: ptr to start of a singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *head = NULL, *current = NULL;
	int cycle;

	cycle = 0;
	head = list;

	current = list;
	while (current->next != NULL)
	{
		if (current->next == head)
		{
			++cycle;
			return (cycle);
		}
		current = current->next;
	}

	return (cycle);
}
