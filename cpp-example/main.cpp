#include <iostream>
#include <sys/utsname.h>
#include <sys/sysinfo.h>
#include <sys/statvfs.h>

int main() {
    // Get the OS name and version using uname()
    struct utsname os_info;
    uname(&os_info);
    std::string os_name = os_info.sysname;
    std::string os_version = os_info.release;

    // Get the CPU usage using getloadavg()
    double cpu_load[3];
    getloadavg(cpu_load, 3);
    double cpu_usage = cpu_load[0];

    // Get the RAM usage using sysinfo()
    struct sysinfo mem_info;
    sysinfo(&mem_info);
    long ram_total = mem_info.totalram;
    long ram_free = mem_info.freeram;
    long ram_used = ram_total - ram_free;
    double ram_usage = (double) ram_used / ram_total;

    // Get the storage usage using statvfs()
    struct statvfs fs_info;
    statvfs("/", &fs_info);
    long fs_total = fs_info.f_blocks * fs_info.f_frsize;
    long fs_free = fs_info.f_bfree * fs_info.f_frsize;
    long fs_used = fs_total - fs_free;
    double fs_usage = (double) fs_used / fs_total;

    // Print the results
    std::cout << "OS Name: " << os_name << std::endl;
    std::cout << "OS Version: " << os_version << std::endl;
    std::cout << "CPU Usage: " << cpu_usage << std::endl;
    std::cout << "RAM Usage: " << ram_usage << std::endl;
    std::cout << "Storage Usage: " << fs_usage << std::endl;

    return 0;
}
