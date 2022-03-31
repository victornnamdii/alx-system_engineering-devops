Describing scripts
 0-iam_betty changes the current user to betty
1-who_am_i prints effective current user id
2-groups prints all group ids of current user
 3-new_owner changes owner of hello to betty
4-empty creates an empty file called hello
5-execute grants execute permission for hello to owner
6-multiple_permission adds execute permission to user and group and adds read permission to others
 7-everybody gives all permissions to everybody
8-James_Bond gives zero permissions to group and owner, but all permissions to others
9-John_Doe gives -rwxr-x-wx permissions to hello
10-mirror_permissions copies the permissions of olleh into hello
11-directories_permissions gives subdirectories only permissions only to everybody
12-directory_permissions creates a my_dir with 751 permission
13-change_group changes the group owners of hello to school
100-change_owner_and_group changes owner to vincent and group owner to staff for all in dir
101-symbolic_link_permissions changes owner to vincent and group to staff for the symbolic link _hello
102-if_only changes owner of hello to betty if it is permitted by guillaume
103-Star_Wars plays star wars episode IV in the terminal
