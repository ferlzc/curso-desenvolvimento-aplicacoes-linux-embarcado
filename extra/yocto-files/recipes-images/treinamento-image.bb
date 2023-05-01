LICENSE = "MIT"

#CORE_IMAGE_BASE_INSTALL:append = "gtk+3-demo"
#CORE_IMAGE_BASE_INSTALL:append = "${@bb.utils.contains('DISTRO_FEATURES', 'x11', 'weston-xwayland matchbox-terminal', '', d)}"

#IMAGE_FEAURES:append = "splash package-management ssh-server-dropbear hwcodecs weston"
IMAGE_FEAURES:append = "splash"

IMAGE_INSTALL:append = " kernel-modules python3 python3-flask python3-paho-mqtt python3-periphery python3-pyzmq nginx \
                         packagegroup-basic \
                         raspi-gpio ${@bb.utils.contains('DISTRO_FEATURES', 'systemd', ' systemd-analyze', '', d)}"

QB_MEM = "-m 512"

add_rootfs_version() {
    printf "TREINAMENTO EMC LOGIC LINUX \\\n \\\l\n" > ${IMAGE_ROOTFS}/etc/issue
    printf "TREINAMENTO EMC LOGIC LINUX %%h\n" > ${IMAGE_ROOTFS}/etc/issue.net
    printf "TREINAMENTO EMC LOGIC LINUX \n\n" >> ${IMAGE_ROOTFS}/etc/issue
    printf "TREINAMENTO EMC LOGIC LINUX \n\n" >> ${IMAGE_ROOTFS}/etc/issue.net
    echo "rasp-treinamento-2023" >> ${IMAGE_ROOTFS}/etc/hostname
}

ROOTFS_POSTPROCESS_COMMAND += " add_rootfs_version;"

inherit core-image
