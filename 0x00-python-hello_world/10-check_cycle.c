#include "lists.h"

/**
 * check_cycle - checks if a singly
 * linked list has a cycle in it
 * @list: pointer to head of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ke, *sw;

	ke = list;
	sw = list;
	while (sw && sw->next)
	{
		ke = ke->next;
		sw = sw->next->next;
		if (ke == sw)
			return (1);
	}
	return (0);
}
