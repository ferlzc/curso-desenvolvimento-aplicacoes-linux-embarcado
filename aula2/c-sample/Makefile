CFLAGS = -Wall -Wextra

TARGET = hello_world_embarcado

all: $(TARGET)

$(TARGET): main.c
	$(CC) $(CFLAGS) -o $(TARGET) main.c

clean:
	rm -f $(TARGET)
