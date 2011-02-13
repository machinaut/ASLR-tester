/* launch process
 * get pid
 * /proc/pid/mmap
 * tells where addr of each libraries
 * look for libc
 * log to output
 */
#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>
#include<stdlib.h>

int main(int argc, char *argv[]) {
  /* Check for arguments */
  if (argc < 2) { puts("Run with executable and arguments."); exit(1); }

  pid_t pid = fork();
  if (pid < 0) { puts("ERROR: Failed to fork."); exit(1); }
  else if (pid == 0) { // child
    int 
    if (argc > 2)

  puts("YAAAY");

  return EXIT_SUCCESS;
}

