# ssh config with puppet

include ssh


class { 'ssh::server':
  validate_sshd_file => true,
  options            => {
    'IdentityFile'           => '~/.ssh/school',
    'PasswordAuthentication' => 'no',
  },
}
