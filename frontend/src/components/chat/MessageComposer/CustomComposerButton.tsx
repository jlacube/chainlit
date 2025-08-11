import React from 'react';
import { useRecoilValue } from 'recoil';

import { sessionState } from '@chainlit/react-client';

import { Button } from '@/components/ui/button';

import { IComposerButton } from '@/types/composerButton';

interface CustomComposerButtonProps {
  button: IComposerButton;
  disabled?: boolean;
}

const CustomComposerButton: React.FC<CustomComposerButtonProps> = ({
  button,
  disabled = false
}) => {
  const session = useRecoilValue(sessionState);

  const handleClick = () => {
    if (session?.socket) {
      session.socket.emit('composer_button_click', {
        button_id: button.id,
        data: button.data || {}
      });
    }
  };

  const getVariant = () => {
    switch (button.style) {
      case 'primary':
        return 'default';
      case 'secondary':
        return 'secondary';
      case 'outline':
        return 'outline';
      default:
        return 'outline';
    }
  };

  return (
    <Button
      variant={getVariant()}
      size="sm"
      disabled={disabled}
      onClick={handleClick}
      className="hover:bg-muted"
    >
      <span className="text-xs">{button.label}</span>
    </Button>
  );
};

export default CustomComposerButton;
