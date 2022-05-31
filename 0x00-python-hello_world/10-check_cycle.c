#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: ptr to start of a singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *head = list, *current_node = list;

	while (head != NULL && head->next != NULL)
	{
		while (current_node->next != NULL)
		{
			/* does the current node point to itself */
			if (current_node->next == head)
				return (1);
			current_node = current_node->next;
		}

		head = head->next;
		current_node = head;
	}

	return (0);
}
