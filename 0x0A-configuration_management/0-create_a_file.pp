# Creating a file in /tmp/holberton
file { '/tmp/holberton':
path    => '/tmp/holberton',
content => 'I love Puppet',
owner   => 'www-data',
group   => 'www-data',
mode    => '0744'
}
