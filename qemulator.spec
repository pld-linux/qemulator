%define		_realname   Qemulator
Summary:	GTK2 GUI for qemu
Summary(pl.UTF-8):	GUI w GTK dla qemu
Name:		qemulator
Version:	0.4.5
Release:	0.9
License:	GPL v2
Group:		X11/Applications
Source0:	http://qemulator.createweb.de/plugins/downloads/dodownload.php?file=%{_realname}-%{version}.tar.gz
# Source0-md5:	a9ea901b8e1a9c5d5087220bd8b4f3ed
URL:		http://qemulator.createweb.de/
Requires:	libglade2 >= 2.5.0
Requires:	python-pygtk-gtk >= 2.8.0
Requires:	python-pygtk-glade >= 2.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qemulator is a full featured emulation suite for the qemu virtual
engine, with on demand job control written in python GTK/Glade2.
Qemulator provides an easy and fast to use image and device
management, a "My machines" list and interactive job control.

It comes with a list of all running jobs from where you can open the
contol panel for each job and perform on demand action. Full
interaction for mounted volumes, usb devices, keyboard and mouse
interaction, screenshots, wave capture and save/restore machine state
and open vnc viewer is provided.

Main Features:
    - Qemulator provides a list view of all qemu-images in your selected
      default images folder.
    - All images on your harddisk can be addet to my machines list, the
      "bookmarks" of Qemulator under a given name and with an icon, even if
      they are not in the default folder or not configured yet.
    - It's possible to store all emulation settings for each image. These
      settings will be loaded each time you select these image for usage.
    - Extra command line for custom qemu options. These extra options will
      also be stored with your settings for the image.

%description -l pl.UTF-8
Qemulator to pełnowartościowy pakiet emulacyjny dla wirtualnego
silnika qemu, z kontrolą zadań na rządzanie napisaną przy pomocy
pythona w GTK/Glade2. Qemulator dostarcza łatwego i szybkiego w
użyciu zarządzania urządzeniami, listę "Moich maszyn" oraz
interaktywną kontrolę zadań.

Dostarczony jest wraz z listą wszystkich uruchomionych zadań skąd
możesz uruchomić panel kontrolny dla każdego zadania i
przeprowadzić akcje na żądanie. Pełna interakcja dla zamontowanych
wolumenów, urządzeń USB, interakcja z myszką i klawiaturą, zrzuty
ekrany, przechwytywanie dźwięku i zachowanie/odtwarzanie stanu
maszyn i otwieranie klienta VNC jest dostarczone.

Główne Cechy:
    - Qemulator dostarcza listę wszystkich obrazów qemu w twoim katalogu
      domyślnym obrazów.
    - Wszystkie obrazy na twoim dysku twardym mogą być dodane do listy
      maszyn, zakładek pod zadaną nazwą i ikoną, nawet gdy nie są w
      domyślnym katalogu albo nie są jeszcze skonfigurowane.
    - Jest możliwe przechowywanie wszystkich ustawień emulacji dla
      każdego obrazu. Te ustawienia będą załadowane za każdym razem jak
      wybierzesz ten obraz do użytku.
    - Dodatkowe komendy linii poleceń dla własnych opcji qemu. Te
      dodatkowe opcję będą również przechowywane z twoimi ustawieniami
      dla tego obrazu.

%prep
%setup -q -n %{_realname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

cp -r usr/local/{bin,lib,share} $RPM_BUILD_ROOT%{_prefix}
mv usr/local/share/%{name}/icons/README usr/local/share/%{name}/icons/README-icons

%find_lang %{_realname}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{_realname}.lang
%defattr(644,root,root,755)
%doc README usr/local/share/%{name}/icons/README-icons
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/qemulator.py
%{_libdir}/%{name}/*
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/*/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%dir %{_pixmapsdir}/%{name}
%{_pixmapsdir}/%{name}/*.png
%{_pixmapsdir}/%{name}/*.svg
%{_pixmapsdir}/%{name}.svg
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.png
%dir %{_datadir}/%{name}/icons/
%{_datadir}/%{name}/icons/*.png
