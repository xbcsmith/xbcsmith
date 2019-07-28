# Resize LVM

## TL;DR

Resize or create a new partition

```bash
fdisk /dev/nvme0n1
```

Extend the pv and lv and resize2fs

```bash
pvs
pvresize /dev/nvme0n1p2
vgs
lvs
lvextend -L+100G /dev/fedora/home
resize2fs /dev/fedora/home
```

## Extend Old Partition

List partition table

```bash
fdisk -l /dev/nvme0n1
```
Example

```
Disk /dev/nvme0n1: 931.5 GiB, 1000204886016 bytes, 1953525168 sectors
Disk model: CT1000P1SSD8                            
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x5e54e860

Device         Boot   Start       End   Sectors   Size Id Type
/dev/nvme0n1p1 *       2048   2099199   2097152     1G 83 Linux
/dev/nvme0n1p2      2099200 937701375 935602176 446.1G 8e Linux LVM
```

Seriously this time

```bash
fdisk /dev/nvme0n1
```

Delete the partition

```
Command (m for help): d
Partition number (1,2, default 2): 2 

Partition 2 has been deleted.
```

Create a new partition

```
Command (m for help): n 

Partition type: 
  p  primary (1 primary, 0 extended, 3 free) 
  e  extended 
Select (default p): *Enter* 
```

List the new partition

```bash
fdisk -l /dev/nvme0n1
```

Results 

```
Disk /dev/nvme0n1: 931.5 GiB, 1000204886016 bytes, 1953525168 sectors
Disk model: CT1000P1SSD8                            
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x5e54e860

Device         Boot   Start        End    Sectors   Size Id Type
/dev/nvme0n1p1 *       2048    2099199    2097152     1G 83 Linux
/dev/nvme0n1p2      2099200 1953523711 1951424512 930.5G 8e Linux LVM
```


## Add New Partition

see above without the delete

### Resize the pv

Display the PV

```bash
pvdisplay
```
Results

```
  --- Physical volume ---
  PV Name               /dev/nvme0n1p2
  VG Name               fedora
  PV Size               <446.13 GiB / not usable 1.00 MiB
  Allocatable           yes 
  PE Size               4.00 MiB
  Total PE              114209
  Free PE               48728
  Allocated PE          65481
  PV UUID               8QkAPp-eO5T-azay-7BEI-cnso-zt2q-SELaln

```

Resize the PV

```bash
pvresize /dev/nvme0n1p2
```

Results

```
  Physical volume "/dev/nvme0n1p2" changed
  1 physical volume(s) resized or updated / 0 physical volume(s) not resized
```

Display the PV

```bash
pvdisplay
```

Results

```
  --- Physical volume ---
  PV Name               /dev/nvme0n1p2
  VG Name               fedora
  PV Size               930.51 GiB / not usable 3.00 MiB
  Allocatable           yes 
  PE Size               4.00 MiB
  Total PE              238210
  Free PE               172729
  Allocated PE          65481
  PV UUID               8QkAPp-eO5T-azay-7BEI-cnso-zt2q-SELaln
```

## Extend the LV

```bash
lvdisplay /dev/fedora/home
```

```
  --- Logical volume ---
  LV Path                /dev/fedora/home
  LV Name                home
  VG Name                fedora
  LV UUID                5svM0K-e11d-2wr0-awDV-Tp7h-nTrJ-g1lbJ8
  LV Write Access        read/write
  LV Creation host, time localhost-live, 2019-03-17 13:47:55 -0400
  LV Status              available
  # open                 1
  LV Size                103.04 GiB
  Current LE             26379
  Segments               2
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           253:2
```

```bash
lvextend -L+100G /dev/fedora/home
```

```
  Size of logical volume fedora/home changed from 103.04 GiB (26379 extents) to 203.04 GiB (51979 extents).
  Logical volume fedora/home successfully resized.
```

```bash
 lvdisplay /dev/fedora/home
```

```
  --- Logical volume ---
  LV Path                /dev/fedora/home
  LV Name                home
  VG Name                fedora
  LV UUID                5svM0K-e11d-2wr0-awDV-Tp7h-nTrJ-g1lbJ8
  LV Write Access        read/write
  LV Creation host, time localhost-live, 2019-03-17 13:47:55 -0400
  LV Status              available
  # open                 1
  LV Size                203.04 GiB
  Current LE             51979
  Segments               2
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           253:2
```

## Resize the Filesystem

```bash
resize2fs /dev/fedora/home 
```

```
resize2fs 1.44.6 (5-Mar-2019)
Filesystem at /dev/fedora/home is mounted on /home; on-line resizing required
old_desc_blocks = 13, new_desc_blocks = 26
The filesystem on /dev/fedora/home is now 53226496 (4k) blocks long.
```

```bash
df -h /dev/fedora/home 
```

```
Filesystem               Size  Used Avail Use% Mounted on
/dev/mapper/fedora-home  200G   27G  165G  14% /home
```
