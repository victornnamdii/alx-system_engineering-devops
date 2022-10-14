# Kills a process called 'killmenow'

exec { 'pkill killmenow':
  command => '/usr/bin/pkill -f /killmenow'
}
