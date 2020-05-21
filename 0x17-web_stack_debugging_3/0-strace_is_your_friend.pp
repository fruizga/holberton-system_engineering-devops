# Changing file extension
exec { 'Changing file ext':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => ['/bin']
}
