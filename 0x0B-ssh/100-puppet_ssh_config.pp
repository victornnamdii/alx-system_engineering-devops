# ssh config with puppet

file { '/etc/ssh/sshd_config':
  ensure => present,
}
-> file_line { 'Append a line to sshd_config':
  path  => '/etc/ssh/sshd_config',
  line  => 'PasswordAuthentication no',
  match => 'PasswordAuthentication',
}
-> file_line { 'Append a line to sshd_config':
  path  => '/etc/ssh/sshd_config',
  line  => 'IdentityFile ~/.ssh/school',
  match => 'IdentityFile',
}
