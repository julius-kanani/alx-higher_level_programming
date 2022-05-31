#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: ptr to start of a singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *head = list, *current_node = NULL;

	while (head != NULL)	/* if head exists */
	{
		current_node = head;	/* head is the current node */
		while (current_node != NULL)
		{
			/* if current node points to the head */
			if (current_node->next == head)
				return (1);
			/* if it does not move to the next node */
			current_node = current_node->next;
		}

		head = head->next;
	}

	return (0);
}
