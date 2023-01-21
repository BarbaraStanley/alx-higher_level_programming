#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: a singly-linked list
 *
 * Return: If there is no cycle - 0
 *         If there is a cycle - 1
 */

int check_cycle(listint_t *list)
{
	listint_t *t, *b;

	if (list == NULL || list->next == NULL)
		return (0);

	t = list->next;
	b = list->next->next;

	while (t && b && b->next)
	{
		if (t == b)
			return (1);

		t = t->next;
		b = b->next->next;
	}

	return (0);
}
