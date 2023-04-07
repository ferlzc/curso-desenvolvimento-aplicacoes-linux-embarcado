#include <linux/module.h>
#include <linux/kernel.h>

/***************Funções de Módulo****************/

MODULE_LICENSE("GPL");

static int hello_world_init(void)
{
    printk(KERN_ALERT "MÓDULO INICIALIZADO!");
    printk("Hello, world! Treinamento Linux Embarcado!\n");
    return 0;
}

static void hello_world_exit(void)
{
    printk(KERN_ALERT "MÓDULO REMOVIDO!");
    printk("Goodbye, world! Treinamento Linux Embarcado!\n");
}

module_init(hello_world_init);
module_exit(hello_world_exit);