# ssh config with puppet

sshd_config {
  'IdentityFile':
    value => '~/.ssh/school',
    ;

  'PasswordAuthentication':
    value => 'no',
    ;
}

purge { 'sshd_config': }
